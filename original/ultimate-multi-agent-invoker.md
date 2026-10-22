---
name: ultimate-multi-agent-invoker
description: >
  Coordinate authorized parallel agents with bounded tasks, explicit ownership, real process verification, actual usage accounting and safe integration. Use when parallel agent work is requested or otherwise authorized.
argument-hint: "[task-scope | plan-file | integration]"
---

Apply the [shared execution and evidence contract](resources/ultimate-shared/execution-contract.md) when coordinating tools, state, verification or recovery. Preserve the user's established requirements and authorization. Research always requires all 15 prescribed provider inputs.


# Multi-agent execution and integration

Use for explicitly requested or otherwise authorized parallel work. Preserve inherited user authorization; a separate plan-approval ritual is not required for already-authorized work. Do not spawn more workers than the host supports, or imply the prompt itself enforces isolation, budget limits or permissions.

## Inputs and ownership

Record objective, accepted constraints, dependencies, base revision, existing dirty/index state, supported agent APIs, concurrency, write ownership and task/aggregate budgets. Check whether agents share files, environment, database, ports or secrets. Read-only investigations may share a workspace. Give concurrent writers actual isolated workspaces when supported, or a verified ownership/serialization scheme appropriate to the host. Do not pretend a worktree isolates databases or external side effects.

Each task records stable ID, scope fingerprint, prerequisites, owner, allowed files/resources, planned verification, deadline, actual state/evidence, usage and recovery action. Keep `pending`, `running`, `blocked`, `failed`, `cancelled`, `complete` separate. A completed task contains evidence; a proposed command does not count.

## Scheduler and integration contract

This sequence is **orchestration pseudocode**, not an implemented SDK:

```text
while unfinished tasks exist:
  observe cancellation, deadlines and actual aggregate budget
  classify finished workers from their real result/check evidence
  mark descendants of failed prerequisites blocked
  dispatch only ready tasks within host/resource limits
  preserve checkpoints and uncertain side-effect receipts
  stop with explicit incomplete state if no safe progress remains

for accepted writer results in dependency order:
  inspect diff against the recorded base
  integrate on the authorized target branch, preserving unrelated work
  resolve semantic conflicts by reading contracts and affected consumers
  run checks on the integrated result
  clean up only an owned, clean and integrated worktree
```

Do not mechanically union imports/types/routes and call it a semantic merge: ordering, registration collisions and incompatible contracts can break despite a clean text merge. Use language-aware tools only when available and validate the final behavior. Builders run their own checks; an independent reviewer is additional evidence for consequential changes, not a prohibition on self-testing. Do not allocate standby guardians/verifiers universally when actual capacity and risk do not justify them.

## Process verification example

The following dependency-free Python example runs modest local verification commands without a shell and preserves raw output in the returned result. Success comes from process status, never substring matching. For large/untrusted outputs use the host's bounded streaming/log artifact facility; this small example buffers output and does not provide that facility. Check arguments/output for secrets before persistence.

```python
from dataclasses import dataclass
from pathlib import Path
import subprocess

@dataclass(frozen=True)
class CheckResult:
    argv: tuple[str, ...]
    cwd: str
    status: str
    exit_code: int | None
    stdout: str
    stderr: str

def _text(value):
    if value is None:
        return ""
    return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else value

def run_check(argv, cwd, timeout_seconds=60):
    if not argv or any(not isinstance(arg, str) for arg in argv):
        raise ValueError("argv must be a nonempty list of strings")
    if timeout_seconds <= 0:
        raise ValueError("timeout must be positive")
    working_dir = str(Path(cwd).resolve(strict=True))
    try:
        result = subprocess.run(
            list(argv), cwd=working_dir, shell=False,
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=timeout_seconds, check=False,
        )
    except subprocess.TimeoutExpired as error:
        return CheckResult(tuple(argv), working_dir, "timeout", None,
                           _text(error.stdout), _text(error.stderr))
    except OSError as error:
        return CheckResult(tuple(argv), working_dir, "failed_to_start", None,
                           "", str(error))
    return CheckResult(tuple(argv), working_dir,
                       "passed" if result.returncode == 0 else "failed",
                       result.returncode, result.stdout, result.stderr)

def summarize_check(result, limit=1000):
    # A summary cannot override the original status or discard raw evidence.
    return {"status": result.status, "exit_code": result.exit_code,
            "argv": list(result.argv), "cwd": result.cwd,
            "stdout_excerpt": result.stdout[:limit],
            "stderr_excerpt": result.stderr[:limit]}
```

Exit zero proves only that command succeeded. Confirm it exercised the required assertion/behavior; a script that merely prints “verified” cannot establish a feature works. Record test selection, baseline failures and actual assertion counts when exposed. On cancellation stop owned subprocesses through the host's supported process-tree controls; a timeout on a parent process alone may leave children alive.

## Actual usage and budgets

Use configurable limits justified by user cost/time constraints; no fixed 50k-token, 12k/minute or depth-two threshold is universally safe. Include retries, failed calls and descendants. Discover whether input/output/cached/thinking usage and money are actually exposed; record unavailable fields as unknown.

The example below is a **post-call accounting guard**, not a full runtime limiter. Wire it to every real usage event. It rejects further work after a trip but cannot undo already-consumed tokens. For a hard pre-call cap reserve a conservative input/output allowance atomically across workers, set provider output limits and reconcile actual usage; without enforceable provider hooks report that hard enforcement is unavailable.

```python
from collections import deque
import time

class UsageBudget:
    def __init__(self, task_limit, aggregate_limit, per_minute_limit, clock=time.monotonic):
        if min(task_limit, aggregate_limit, per_minute_limit) <= 0:
            raise ValueError("limits must be positive")
        self.task_limit = task_limit
        self.aggregate_limit = aggregate_limit
        self.per_minute_limit = per_minute_limit
        self.clock = clock
        self.by_task = {}
        self.total = 0
        self.events = deque()
        self.tripped = False

    def record(self, task_id, tokens):
        if not isinstance(task_id, str) or not task_id:
            raise ValueError("task ID is required")
        if type(tokens) is not int or tokens < 0:
            raise ValueError("actual tokens must be a nonnegative integer")
        now = self.clock()
        self.by_task[task_id] = self.by_task.get(task_id, 0) + tokens
        self.total += tokens
        self.events.append((now, tokens))
        while self.events and self.events[0][0] <= now - 60:
            self.events.popleft()
        rate = sum(count for _, count in self.events)
        self.tripped = self.tripped or (
            self.by_task[task_id] > self.task_limit
            or self.total > self.aggregate_limit
            or rate > self.per_minute_limit
        )
        return not self.tripped
```

This class is for a single serialized accounting owner. Concurrent workers must send usage to that owner or use a transaction/lock; each worker's private counter cannot enforce an aggregate limit. Persist counts, trips and window timestamps in durable task state for restart; the in-memory example does not provide persistence. Wall-clock deadlines, money, recursion and tool-call limits are separate controls to implement in the actual runtime.

## Safe worktree teardown example

Provision worktrees only within the authorized repository, using unique recorded paths/branches. Capture their ownership when created. Never default to `remove --force`, `branch -D`, or hard reset. Preserve failed work and raw logs until diagnosis/handoff is complete.

```python
from pathlib import Path
import subprocess

def remove_owned_integrated_worktree(repo, candidate, owned):
    """owned maps exact resolved worktree paths to their recorded branch names."""
    repo = Path(repo).resolve(strict=True)
    candidate = Path(candidate).resolve(strict=True)
    root = (repo / ".worktrees").resolve()
    if repo not in root.parents:
        raise ValueError("worktree root resolves outside the repository")
    if candidate == root or root not in candidate.parents:
        raise ValueError("worktree is outside the owned worktree root")
    branch = owned.get(str(candidate))
    if not branch:
        raise ValueError("worktree ownership is not recorded")

    def git(*args):
        return subprocess.run(["git", "-C", str(repo), *args],
                              check=True, capture_output=True, text=True)

    top = git("-C", str(candidate), "rev-parse", "--show-toplevel").stdout.strip()
    if Path(top).resolve() != candidate:
        raise ValueError("candidate is not a worktree root")
    actual_branch = git("-C", str(candidate), "symbolic-ref", "--short", "HEAD").stdout.strip()
    if actual_branch != branch:
        raise ValueError("worktree branch differs from recorded ownership")
    state = git("-C", str(candidate), "status", "--porcelain",
                "--untracked-files=all", "--ignored").stdout
    if state.strip():
        raise ValueError("worktree contains tracked, untracked or ignored work; preserve it")
    git("merge-base", "--is-ancestor", branch, "HEAD")
    git("worktree", "remove", str(candidate))
    # Retain the branch for recovery. Delete separately with ordinary -d only if authorized.
```

This example assumes a trusted local filesystem during the check/remove sequence; concurrent modifications require scheduler exclusion. Worktree removal never substitutes for checking actual integration and tests. Scope verification and ownership checks must be implemented in the actual host, not inferred from prompt text.

## Completion and recovery

Return task statuses, integrated revisions, changed artifacts, real verification evidence, observed usage and unavailable metrics, retained failed work and next actions. If a dependency, quota or provider remains missing, report incomplete. Do not claim token reductions, conflict-elimination percentages, guaranteed recovery or runtime support without measured, reproducible evidence. Push/deploy only when authorized.
