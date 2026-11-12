"""Install this repository's Codex skill without overwriting an existing skill."""

import argparse
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=Path.home() / ".codex" / "skills",
        help="Codex skills directory (default: ~/.codex/skills)",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    slug = "mckinsey-rewired-ai-transformation"
    source = root / "skills" / slug
    target = args.skills_dir.expanduser().resolve() / slug
    if not (source / "SKILL.md").is_file():
        parser.exit(1, f"Package is incomplete: {source / 'SKILL.md'}\n")
    if target.exists() or target.is_symlink():
        parser.exit(1, f"Already exists; no files changed: {target}\n")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)
    print(f"Installed: {target}")
    print("Start a new Codex chat if the skill does not appear immediately.")


if __name__ == "__main__":
    main()
