#!/usr/bin/env python3
"""Resolve local repository identity and a private Notion binding. No network writes."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit
from uuid import UUID


def canonical_repository(remote):
    """Normalize equivalent network remotes without retaining credentials."""
    value = remote.strip()
    if not value or any(char.isspace() for char in value) or re.match(r"^[A-Za-z]:[\\/]", value):
        raise ValueError("A network repository remote is required")
    if "://" in value:
        try:
            parts = urlsplit(value)
            port = parts.port
        except ValueError as exc:
            raise ValueError("Invalid repository remote") from exc
        if parts.scheme not in {"https", "http", "ssh", "git"} or not parts.hostname:
            raise ValueError("Unsupported repository remote")
        host = parts.hostname.lower()
        if ":" in host:
            host = "[" + host + "]"
        default = {"https": 443, "http": 80, "ssh": 22, "git": 9418}[parts.scheme]
        if port and port != default:
            host += ":" + str(port)
        path = parts.path
    else:
        match = re.fullmatch(r"(?:[^@/\s]+@)?([^:/\s]+):([^\s]+)", value)
        if not match:
            raise ValueError("Unsupported repository remote")
        host, path = match.groups()
        host = host.lower()
    path = path.strip("/")
    if path.endswith(".git"):
        path = path[:-4]
    if not path or "/" not in path or any(part in {"", ".", ".."} for part in path.split("/")):
        raise ValueError("Repository namespace and name are required")
    if host == "github.com":
        path = path.lower()
    return "repo:" + host + "/" + path


def git(directory, *args):
    try:
        result = subprocess.run(
            ["git", "-C", str(directory), *args],
            check=False, capture_output=True, text=True, timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ValueError("Repository metadata is unavailable") from exc
    if result.returncode:
        raise ValueError("Cannot read the requested repository metadata")
    return result.stdout.strip()


def identify(directory, remote_name=None):
    root = Path(git(directory, "rev-parse", "--show-toplevel")).resolve()
    remotes = git(root, "remote").splitlines()
    selected = remote_name or ("origin" if "origin" in remotes else remotes[0] if len(remotes) == 1 else None)
    if not selected or selected not in remotes:
        raise ValueError("Select a repository remote explicitly when none or several are available")
    key = canonical_repository(git(root, "remote", "get-url", selected))
    return {"project_key": key, "repository_root": str(root), "remote_name": selected}


def default_registry():
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA")
        if not base:
            raise ValueError("LOCALAPPDATA is unavailable; provide --registry")
        return Path(base) / "UltimateWorkflows" / "notion-projects.json"
    base = Path(os.environ.get("XDG_STATE_HOME", str(Path.home() / ".local/state")))
    return base / "ultimate-workflows" / "notion-projects.json"


def resolve_binding(identity, registry):
    try:
        config = json.loads(Path(registry).read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as exc:
        raise ValueError("Private Notion registry is unavailable or invalid") from exc
    if not isinstance(config, dict) or config.get("schema_version") != 1 or not isinstance(config.get("projects"), dict):
        raise ValueError("Unsupported private Notion registry schema")
    binding = config["projects"].get(identity["project_key"])
    if not isinstance(binding, dict):
        raise ValueError("Project is unbound; resolve its Notion destination before implementation")
    if binding.get("tracking_mode") != "strict":
        raise ValueError("The stored binding must explicitly use strict tracking")
    try:
        page_id = UUID(binding["project_page_id"])
        page_url = urlsplit(binding["project_url"])
        if page_url.scheme != "https" or page_url.hostname not in {"notion.so", "www.notion.so", "app.notion.com"}:
            raise ValueError("Invalid Notion project URL")
        if page_url.username or page_url.password:
            raise ValueError("Credentials are not allowed in project URLs")
        match = re.search(r"([0-9a-fA-F]{32})/?$", page_url.path.replace("-", ""))
        if not match or UUID(match.group(1)) != page_id:
            raise ValueError("Notion project URL and page ID disagree")
        for field in ("tasks_data_source_url", "docs_data_source_url"):
            value = binding[field]
            if not isinstance(value, str) or not value.startswith("collection://"):
                raise ValueError("A Notion collection URL is required")
            UUID(value.removeprefix("collection://"))
    except (KeyError, TypeError, AttributeError, ValueError) as exc:
        raise ValueError("Project binding contains invalid or inconsistent Notion IDs") from exc
    return {**identity, "binding": binding, "status": "binding_resolved"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("identify", "resolve"))
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--remote")
    parser.add_argument("--registry", type=Path)
    args = parser.parse_args()
    try:
        result = identify(args.repo, args.remote)
        if args.command == "resolve":
            result = resolve_binding(result, args.registry if args.registry is not None else default_registry())
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except ValueError as exc:
        print(json.dumps({"status": "blocked", "reason": str(exc)}))
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
