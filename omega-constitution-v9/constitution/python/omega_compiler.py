#!/usr/bin/env python3
"""
OMEGA COMPILER — Project Handoff Tool

Strips away the Omega framework and exports a clean, shareable project.
The recipient gets just the code, not the constitution.
"""

import os
import shutil
from datetime import datetime

# Path setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONSTITUTION_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(CONSTITUTION_DIR)
USER_SPACE = os.path.join(ROOT_DIR, "USER SPACE")
DESKTOP_DIR = os.path.expanduser("~/Desktop")

# What to EXCLUDE (Omega framework stuff)
EXCLUDE_FILES = {
    'SESSION_CONTEXT.md',
    'TRACKER.md',
    'STATE.md',
    'rules.md',
    'decisions.md',
    'deps.md',
    '.DS_Store',
}

EXCLUDE_DIRS = {
    'seed',
    'plug-and-play',
    'phases',
    '00_governance',
    '01_discovery',
    '.git',
    '__pycache__',
    'node_modules',
}

# What to INCLUDE from docs (optionally)
INCLUDE_DOCS = {
    'PRD.md',
    'TECH_SPEC.md',
    'ARCHITECTURE.md',
    'API.md',
}


def get_project_info():
    """Try to read project info from seeds."""
    project_md = os.path.join(USER_SPACE, "seed", "PROJECT.md")
    info = {"name": "Project", "description": ""}

    if os.path.exists(project_md):
        try:
            with open(project_md, 'r', encoding='utf-8') as f:
                content = f.read()
                # Try to extract project name
                for line in content.split('\n'):
                    if 'project name' in line.lower() and ':' in line:
                        info["name"] = line.split(':', 1)[1].strip()
                        break
                    if line.startswith('# '):
                        info["name"] = line[2:].strip()
                        break
        except Exception:
            pass

    return info


def export_project(export_path, include_docs=False):
    """Export USER SPACE, stripping Omega framework files."""

    exported_files = []

    for root, dirs, files in os.walk(USER_SPACE):
        # Filter directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]

        # Calculate relative path
        rel_root = os.path.relpath(root, USER_SPACE)

        if rel_root == '.':
            dest_dir = export_path
        else:
            dest_dir = os.path.join(export_path, rel_root)

        # Filter files
        for f in files:
            if f in EXCLUDE_FILES or f.startswith('.'):
                continue

            # Skip docs unless requested
            if not include_docs and rel_root.startswith('02_docs'):
                if f not in INCLUDE_DOCS:
                    continue

            src = os.path.join(root, f)

            # Create dest directory if needed
            os.makedirs(dest_dir, exist_ok=True)

            # Copy file
            dst = os.path.join(dest_dir, f)
            shutil.copy2(src, dst)
            exported_files.append(os.path.relpath(dst, export_path))

    return exported_files


def generate_readme(export_path, project_name, exported_files):
    """Generate a clean README for the exported project."""

    # Detect project type from files
    has_package_json = any('package.json' in f for f in exported_files)
    has_requirements = any('requirements.txt' in f for f in exported_files)
    has_cargo = any('Cargo.toml' in f for f in exported_files)

    # Generate setup instructions
    if has_package_json:
        setup = "npm install"
        run = "npm run dev"
    elif has_requirements:
        setup = "pip install -r requirements.txt"
        run = "python main.py"
    elif has_cargo:
        setup = "cargo build"
        run = "cargo run"
    else:
        setup = "# Add your setup commands"
        run = "# Add your run command"

    # Build file tree (simplified)
    tree_lines = []
    dirs_seen = set()
    for f in sorted(exported_files)[:20]:  # First 20 files
        parts = f.split(os.sep)
        if len(parts) > 1:
            dir_name = parts[0]
            if dir_name not in dirs_seen:
                tree_lines.append(f"├── {dir_name}/")
                dirs_seen.add(dir_name)
        else:
            tree_lines.append(f"├── {f}")

    if len(exported_files) > 20:
        tree_lines.append(f"└── ... and {len(exported_files) - 20} more files")

    readme = f"""# {project_name}

> Built with the Omega Constitution • Exported {datetime.now().strftime('%Y-%m-%d')}

## Quick Start

```bash
# Install dependencies
{setup}

# Run the project
{run}
```

## Project Structure

```
{project_name}/
{chr(10).join(tree_lines)}
```

## Files Included

- **{len(exported_files)}** files exported
- Framework files stripped
- Ready to deploy

---

*This project was built using the [Omega Constitution](https://github.com/edsworld27/omega-constitution).*
"""

    with open(os.path.join(export_path, "README.md"), 'w', encoding='utf-8') as f:
        f.write(readme)


def generate_handoff_summary(export_path, project_name, exported_files):
    """Generate a handoff summary for the recipient."""

    summary = f"""# Project Handoff: {project_name}

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Files:** {len(exported_files)}

## What's Included

This export contains the clean, deployable project code without the development framework.

## What's NOT Included

The following were stripped during export:
- Development seeds (project requirements, personas, constraints)
- Session context and tracking files
- Governance and decision logs
- Phase planning documents

## If You Need the Full History

The original development was done using the Omega Constitution framework.
Contact the developer for access to the full project history and decision logs.

## Next Steps

1. Review the README.md for setup instructions
2. Install dependencies
3. Configure environment variables (if any)
4. Deploy

---

*Compiled by omega_compiler.py*
"""

    with open(os.path.join(export_path, "HANDOFF.md"), 'w', encoding='utf-8') as f:
        f.write(summary)


def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║             📦 OMEGA COMPILER — PROJECT HANDOFF           ║
╠═══════════════════════════════════════════════════════════╣
║  Strips the framework, exports clean project for sharing  ║
╚═══════════════════════════════════════════════════════════╝
""")

    # Check USER SPACE exists
    if not os.path.exists(USER_SPACE):
        print("❌ Error: USER SPACE folder not found.")
        print(f"   Expected: {USER_SPACE}")
        return

    # Get project info
    info = get_project_info()

    # Get project name
    print(f"Detected project: {info['name']}")
    project_name = input(f"\nProject name [{info['name']}]: ").strip()
    if not project_name:
        project_name = info['name']

    # Ask about docs
    include_docs = input("\nInclude documentation (PRD, specs)? [y/N]: ").strip().lower() == 'y'

    # Create export path
    safe_name = "".join(c if c.isalnum() or c in '-_' else '_' for c in project_name)
    export_path = os.path.join(DESKTOP_DIR, safe_name)

    # Check if exists
    if os.path.exists(export_path):
        print(f"\n⚠️  Folder already exists: {export_path}")
        if input("Overwrite? [y/N]: ").strip().lower() != 'y':
            print("🛑 Aborted.")
            return
        shutil.rmtree(export_path)

    # Export
    print(f"\n📦 Exporting '{project_name}'...")
    os.makedirs(export_path)

    exported_files = export_project(export_path, include_docs)

    if not exported_files:
        print("⚠️  No files found to export.")
        print("   Make sure your code is in USER SPACE (not in seed/ or governance folders)")
        shutil.rmtree(export_path)
        return

    # Generate docs
    generate_readme(export_path, project_name, exported_files)
    generate_handoff_summary(export_path, project_name, exported_files)

    print(f"""
╔═══════════════════════════════════════════════════════════╗
║                     ✅ EXPORT COMPLETE                    ║
╠═══════════════════════════════════════════════════════════╣
║  Files exported: {len(exported_files):>4}                                    ║
║  Location: Desktop/{safe_name:<36} ║
╚═══════════════════════════════════════════════════════════╝

📁 {export_path}

The project is ready to share. Framework stripped.
""")


if __name__ == "__main__":
    main()
