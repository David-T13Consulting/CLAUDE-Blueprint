#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent
AGENTS_DIR = ROOT.parent / ".claude" / "agents"
EXPECTED_FIELDS = {"name", "description", "tools", "model", "maxTurns"}


def parse_agent_file(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    metadata: Dict[str, Any] = {}
    lines = text.splitlines()
    current_key: Optional[str] = None
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            stripped = line.rstrip()
            if stripped.strip() == "---":
                break
            if not stripped.strip():
                continue
            if stripped.lstrip() != stripped:
                # Indented line: possible sequence item
                if current_key and stripped.lstrip().startswith("- "):
                    value = stripped.lstrip()[2:].strip()
                    if isinstance(metadata.get(current_key), list):
                        metadata[current_key].append(value)
                    else:
                        metadata[current_key] = [value]
                continue
            if ":" in stripped:
                key, value = stripped.split(":", 1)
                key = key.strip()
                value = value.strip()
                if value == "":
                    metadata[key] = []
                    current_key = key
                else:
                    metadata[key] = value
                    current_key = None
    return {"path": str(path), "metadata": metadata, "raw": text}


def list_agents() -> List[Dict[str, Any]]:
    if not AGENTS_DIR.exists():
        return []
    return [parse_agent_file(path) for path in sorted(AGENTS_DIR.glob("*.md"))]


def validate_agents() -> Dict[str, Any]:
    agents = list_agents()
    report = {"agents": [], "valid": True}
    for agent in agents:
        metadata = agent["metadata"]
        missing = [field for field in EXPECTED_FIELDS if field not in metadata]
        if missing:
            report["valid"] = False
        report["agents"].append(
            {
                "path": agent["path"],
                "has_frontmatter": bool(metadata),
                "missing_fields": missing,
                "tools": metadata.get("tools", ""),
                "model": metadata.get("model", ""),
            }
        )
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect and validate .claude/agents definitions.")
    parser.add_argument("--list", action="store_true", help="List available agent files.")
    parser.add_argument("--validate", action="store_true", help="Validate agent metadata and expected fields.")
    parser.add_argument("--output", type=str, help="Write the report to a JSON file.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.list:
        agents = list_agents()
        for agent in agents:
            print(agent["path"])
        return 0

    if args.validate:
        report = validate_agents()
        print(json.dumps(report, indent=2))
        if args.output:
            Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
        return 0

    print("Nothing to do. Use --list or --validate.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
