const assert = require('node:assert/strict');
const test = require('node:test');
const fs = require('node:fs');
const path = require('node:path');
const { Readable } = require('node:stream');
const { pipeline } = require('node:stream/promises');
const { spawnSync } = require('node:child_process');
const root = path.resolve(__dirname, '../original');
function source(name, index = 0) {
  const text = fs.readFileSync(path.join(root, `ultimate-${name}-workflow.md`), 'utf8');
  return [...text.matchAll(/```javascript\r?\n([\s\S]*?)```/g)][index][1];
}
function url(src) { return `data:text/javascript;base64,${Buffer.from(src).toString('base64')}`; }
function load(name) { return import(url(source(name, name === "automation" ? 1 : 0))); }
class Loader {
  constructor(batch) { this.batch = batch; this.cache = new Map(); }
  async load(id) {
    if (!this.cache.has(id)) this.cache.set(id, this.batch([id]).then(v => v[0]));
    return this.cache.get(id);
  }
}
function store() {
  const locks = new Map(), values = new Map();
  return { locks, values,
    async get(k) { return values.has(k) ? values.get(k) : null; },
    async set(k, v) { values.set(k, v); },
    async tryAcquire(k, t) { if (locks.has(k)) return false; locks.set(k, t); return true; },
    async releaseIfOwner(k, t) { if (locks.get(k) === t) locks.delete(k); },
  };
}
test('loader is request scoped and tenant filtered, maps missing/shuffled rows', async () => {
  const { createUserLoader } = await load('api');
  const db = { user: { async findMany({where}) {
    return [{ id: 'b', name: where.tenantId + '-b' }, { id: 'a', name: where.tenantId + '-a' }];
  } } };
  const a = createUserLoader({ DataLoader: Loader, db, tenantId: 'A' });
  const b = createUserLoader({ DataLoader: Loader, db, tenantId: 'B' });
  assert.equal((await a.load('a')).name, 'A-a');
  assert.equal((await b.load('a')).name, 'B-a');
  assert.deepEqual((await a.batch(['a','b','none'])).map(x => x?.name ?? null), ['A-a','A-b',null]);
  assert.throws(() => createUserLoader({DataLoader:Loader,db}), /tenant/);
});
test('cache expired owner cannot delete successor token', async () => {
  const { fetchWithStampedeProtection } = await load('caching');
  const cache = store();
  const out = await fetchWithStampedeProtection({ cache, key:'tenant:A:v1:k', fetcher:async () => {
    cache.locks.set('lock:tenant:A:v1:k','successor'); return 7;
  } });
  assert.equal(out,7); assert.equal(cache.locks.get('lock:tenant:A:v1:k'),'successor');
});
test('cache miss bounded contention aborts without recursion', async () => {
  const { fetchWithStampedeProtection } = await load('caching');
  const cache = store(); cache.locks.set('lock:k','held');
  const start = Date.now();
  await assert.rejects(fetchWithStampedeProtection({ cache,key:'k',fetcher:async()=>1,waitMs:35 }));
  assert.ok(Date.now()-start < 1000);
});
test('cache fetch failure releases own token and propagates', async () => {
  const { fetchWithStampedeProtection } = await load('caching'); const cache=store();
  await assert.rejects(fetchWithStampedeProtection({cache,key:'k',fetcher:async()=>{throw Error('backend')}}), /backend/);
  assert.equal(cache.locks.size,0);
});
test('automation owner-safe release and failure propagation', async () => {
  const { withLock } = await load('automation'); const s=store();
  await assert.rejects(withLock({store:s,key:'k',task:async()=>{
    s.locks.set('k','successor'); throw Error('task failed');
  }}),/task failed/);
  assert.equal(s.locks.get('k'),'successor');
});
test('automation rejects invalid deadline and conflict without process exit', async () => {
  const {withLock}=await load('automation');const s=store();s.locks.set('k','held');
  await assert.rejects(withLock({store:s,key:'k',task:async()=>{},timeoutMs:10,leaseMs:5}),RangeError);
  await assert.rejects(withLock({store:s,key:'k',task:async()=>{throw Error('must not run')}}),/Lock conflict/);
});
test('batch sink flushes bounded batches and final partial batch', async()=>{
  const {createBatchSink}=await load('data');const batches=[];
  await pipeline(Readable.from([{v:1},{v:2},{v:3}]),createBatchSink({maxRows:2,flushBatch:async rows=>batches.push(rows)}));
  assert.deepEqual(batches.map(x=>x.length),[2,1]);
});
test('batch write rejection reaches pipeline without hanging',async()=>{
  const {createBatchSink}=await load('data');
  await assert.rejects(pipeline(Readable.from([{v:1}]),createBatchSink({maxRows:1,flushBatch:async()=>{throw Error('DB failed')}})),/DB failed/);
});
test('batch final rejection reaches pipeline and oversize is rejected',async()=>{
  const {createBatchSink}=await load('data');
  await assert.rejects(pipeline(Readable.from([{v:1}]),createBatchSink({flushBatch:async()=>{throw Error('final failed')}})),/final failed/);
  await assert.rejects(pipeline(Readable.from([{v:'long'}]),createBatchSink({maxBytes:20,maxRecordBytes:5,flushBatch:async()=>{}})),/too large/);
});
test('batch byte limit flushes before next record',async()=>{
  const {createBatchSink}=await load('data');const batches=[];
  await pipeline(Readable.from([{v:1},{v:2},{v:3}]),createBatchSink({maxRows:20,maxBytes:14,maxRecordBytes:14,flushBatch:async rows=>batches.push(rows)}));
  assert.deepEqual(batches.map(x=>x.length),[2,1]);
});
test('readiness timeout is bounded and redacted; draining bypasses dependency',async()=>{
  const {installHealth}=await load('deployment');const routes={};let draining=false,calls=0;
  installHealth({get:(k,v)=>routes[k]=v},{probeMs:20,isDraining:()=>draining,checkDependencies:()=>{calls++;return new Promise(()=>{});}});
  function res(){return {status(n){this.code=n;return this},json(o){this.body=o;return this},send(o){this.body=o;return this}}}
  const first=res();await routes['/ready']({},first);assert.equal(first.code,503);assert.deepEqual(first.body,{status:'UNAVAILABLE'});
  draining=true;const second=res();await routes['/ready']({},second);assert.equal(second.code,503);assert.equal(calls,1);
});
test('shutdown hung request reaches hard deadline and graceful path exits success',()=>{
  const src=source('deployment');
  for(const hung of [false,true]){
    const script=`import(${JSON.stringify(url(src))}).then(({installShutdown})=>{installShutdown({server:{close(cb){${hung?'':'cb();'}},closeAllConnections(){console.log('FORCED')}},markDraining(){console.log('DRAIN')},closeResources:async()=>{},deadlineMs:30});process.emit('SIGTERM');});`;
    const result=spawnSync(process.execPath,['-e',script],{encoding:'utf8',timeout:2000});
    assert.ifError(result.error);assert.equal(result.status,hung?1:0);assert.match(result.stdout,/DRAIN/);
    if(hung)assert.match(result.stdout,/FORCED/);
  }
});
