#!/usr/bin/env python3
"""Export reviewed Gemini-source mirrors; no installed skill writes."""
import hashlib
import json
import os
from pathlib import Path
import stat
import tempfile

ROOT = Path(__file__).resolve().parents[1]
QUALITY_WORKFLOWS = {f"ultimate-{name}" for name in (
    "research-workflow", "planning-workflow", "multi-agent-invoker",
    "debugging-workflow", "review-workflow")}

def guard(path):
    path = Path(path).absolute()
    root = ROOT.absolute()
    if not path.is_relative_to(root) or ".." in path.parts or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError("Generated/source path escapes repository")
    current = path
    while current != root:
        if current.exists() or current.is_symlink():
            info = current.lstat()
            if current.is_symlink() or getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
                raise ValueError(f"Symlink/reparse path requires reconciliation: {path}")
            if current != path and not current.is_dir():
                raise ValueError(f"Parent is not a directory: {current}")
        current = current.parent
    return path

def atomic(path, data):
    guard(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
        temporary=Path(stream.name); stream.write(data)
    try: os.replace(temporary, path)
    finally: temporary.unlink(missing_ok=True)

def source_bytes(path):
    value = guard(path).read_bytes()
    if path.suffix in {".md", ".py", ".json", ".js", ".txt", ".yaml", ".yml", ".sh", ".ps1"} and b"\r\n" in value:
        raise ValueError(f"Source must use LF to match committed bundle hashes: {path}")
    return value

def build():
    original, universal = ROOT / "original", ROOT / "universal"
    guard(original); guard(universal)
    sources=sorted(original.glob("ultimate-*.md"))
    if len(sources)!=38: raise ValueError(f"Expected 38 workflows; found {len(sources)}")
    manifest_path=guard(ROOT / "workflow-manifest.json")
    previous=json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {"workflows":{}}
    manifest={"schema_version":1,"authoring_source":"Gemini workflow skills","required_research_inputs":15,"workflows":{}}
    outputs={}
    for source in sources:
        data=source_bytes(source)
        outputs[guard(universal/source.name)]=data
        hashes={"SKILL.md":hashlib.sha256(data).hexdigest()}
        groups = ["ultimate-shared", source.stem]
        if source.stem in QUALITY_WORKFLOWS:
            groups.extend(["ultimate-quality", "ultimate-research-workflow"])
        groups = list(dict.fromkeys(groups))
        for group in groups:
            folder=guard(original/"resources"/group)
            if not folder.is_dir(): continue
            for resource in sorted(folder.rglob("*")):
                guard(resource)
                if not resource.is_file() or "__pycache__" in resource.parts or resource.suffix==".pyc": continue
                relative=resource.relative_to(original)
                value=source_bytes(resource)
                outputs[guard(universal/relative)]=value
                hashes[relative.as_posix()]=hashlib.sha256(value).hexdigest()
        manifest["workflows"][source.stem]={"files":hashes}
    old_resources={relative:sha for item in previous["workflows"].values() for relative,sha in item["files"].items() if relative!="SKILL.md"}
    resources={relative for item in manifest["workflows"].values() for relative in item["files"] if relative!="SKILL.md"}
    removals=[]
    for relative in old_resources.keys()-resources:
        obsolete=guard(universal/relative)
        if not obsolete.is_relative_to(universal): raise ValueError("Obsolete path escapes exports")
        if obsolete.exists():
            if not obsolete.is_file() or hashlib.sha256(obsolete.read_bytes()).hexdigest()!=old_resources[relative]:
                raise ValueError(f"Modified obsolete export requires reconciliation: {relative}")
            removals.append(obsolete)
    outputs[manifest_path]=(json.dumps(manifest,indent=2,sort_keys=True)+"\n").encode("utf-8")
    for path in outputs:
        guard(path)
        if path.exists() and not path.is_file(): raise ValueError(f"Not a regular output file: {path}")
    previous_bytes={path:path.read_bytes() if path.exists() else None for path in [*outputs,*removals]}
    written=[]
    try:
        for path,value in outputs.items():
            atomic(path,value); written.append(path)
        for path in removals:
            guard(path); path.unlink(); written.append(path)
    except Exception:
        for path in reversed(written):
            old=previous_bytes[path]
            if old is None: guard(path).unlink(missing_ok=True)
            else: atomic(path,old)
        raise
    return manifest

if __name__=="__main__":
    result=build()
    print(f"Exported {len(result['workflows'])} workflows with complete resource hashes.")
