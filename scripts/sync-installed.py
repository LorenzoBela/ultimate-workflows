#!/usr/bin/env python3
"""Guarded synchronization of reviewed workflow bundles to local installations.

Requires the private baseline manifest captured before editing. Dry run is default.
Only declared bundle files are written. Unrelated files and UI metadata are kept.
"""
import argparse
import hashlib
import json
import os
import stat
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def guard(path):
    current = Path(path).absolute()
    leaf = current
    while current.parent != current:
        if current.exists() or current.is_symlink():
            info = current.lstat()
            if current.is_symlink() or getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
                raise ValueError("Symlink/reparse destination requires reconciliation")
            if current != leaf and not current.is_dir():
                raise ValueError("Destination parent is not a directory")
        current = current.parent


def digest(data):
    return hashlib.sha256(data).hexdigest()


def atomic_write(path, data):
    guard(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        stream.write(data)
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def plan_sync(manifest, installations):
    published = json.loads((ROOT / "workflow-manifest.json").read_text(encoding="utf-8"))
    changes = []
    for label, directory in installations.items():
        directory = Path(directory).resolve()
        expected = manifest["sources"][label]
        for name, bundle in published["workflows"].items():
            for relative, source_hash in bundle["files"].items():
                source = ROOT / "original" / (f"{name}.md" if relative == "SKILL.md" else relative)
                if ".." in Path(relative).parts or not source.resolve().is_relative_to((ROOT / "original").resolve()):
                    raise ValueError("Source manifest path escapes workflow sources")
                data = source.read_bytes()
                if digest(data) != source_hash:
                    raise ValueError(f"Build manifest is stale for {name}/{relative}; rebuild first")
                destination = directory / name / relative
                guard(destination)
                if not destination.resolve().is_relative_to(directory):
                    raise ValueError("Destination escapes selected installation")
                key = f"{name}/{relative}"
                current = destination.read_bytes() if destination.exists() else None
                if current == data:
                    continue
                if current is not None and (key not in expected or digest(current) != expected[key]):
                    raise ValueError(f"Local customization detected: {label}/{key}; reconcile before syncing")
                # A baseline file removed during this task is also an intentional local change.
                if current is None and key in expected:
                    raise ValueError(f"Baseline file removed locally: {label}/{key}")
                changes.append((destination, data, current))
    return changes


def apply_sync(changes):
    written = []
    try:
        for path, data, old in changes:
            guard(path)
            # Recheck immediately before writing; never silently overwrite a new edit.
            current = path.read_bytes() if path.exists() else None
            if current != old:
                raise ValueError("Installation changed after preflight; rerun after reconciliation")
            atomic_write(path, data)
            written.append((path, data, old))
    except Exception:
        for path, data, old in reversed(written):
            if path.exists() and path.read_bytes() == data:
                if old is None:
                    path.unlink()
                else:
                    atomic_write(path, old)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-manifest", type=Path, required=True)
    parser.add_argument("--gemini-dir", type=Path, required=True)
    parser.add_argument("--codex-dir", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    manifest = json.loads(args.baseline_manifest.read_text(encoding="utf-8"))
    changes = plan_sync(manifest, {"gemini": args.gemini_dir, "codex": args.codex_dir})
    if args.apply:
        apply_sync(changes)
    print(f"{'Applied' if args.apply else 'Dry run:'} {len(changes)} owned bundle file updates; unrelated files preserved.")


if __name__ == "__main__":
    main()
