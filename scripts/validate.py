#!/usr/bin/env python3
"""Validate source metadata, bundle links, export parity and provenance hashes."""
import hashlib
import json
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "workflow-manifest.json").read_text(encoding="utf-8"))
assert len(manifest["workflows"]) == 38
for name, entry in manifest["workflows"].items():
    source = ROOT / "original" / f"{name}.md"
    text = source.read_text(encoding="utf-8-sig")
    assert text.startswith("---\n"), name
    metadata = yaml.safe_load(text.split("---", 2)[1])
    assert metadata["name"] == name and len(name) <= 64, name
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name), name
    assert isinstance(metadata["description"], str) and 0 < len(metadata["description"]) <= 1024, name
    assert not re.search(r"^(<<<<<<<|=======|>>>>>>>)", text, re.M), name
    assert source.read_bytes() == (ROOT / "universal" / source.name).read_bytes(), name
    for relative, expected in entry["files"].items():
        for edition in ["original", "universal"]:
            path = ROOT / edition / (f"{name}.md" if relative == "SKILL.md" else relative)
            assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, str(path)
    for link in re.findall(r"\]\(([^)\s]+)\)", text):
        if link.startswith(("https:", "http:", "#", "mailto:")):
            continue
        assert (source.parent / link.split("#")[0]).exists(), (name, link)
print("Validated 38 metadata records, source/export parity, resource links and bundle hashes.")
