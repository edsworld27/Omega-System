import os
import shutil
from datetime import datetime

# Paths
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
USER_SPACE = os.path.join(ROOT_DIR, "USER SPACE")
DESKTOP_DIR = os.path.expanduser("~/Desktop")

# Files that should NOT be exported (Omega tracking context)
IGNORE_FILES = {
    'SESSION_CONTEXT.md',
    'TRACKER.md',
}
IGNORE_DIRS = {
    'phases',
    'plug-and-play',
    'seed',
    '.DS_Store'
}

def clean_copy_user_space(project_name, export_path):
    """Copies the USER SPACE directory but ignores Omega-specific tracking and seed folders."""
    os.makedirs(export_path, exist_ok=True)
    
    for root, dirs, files in os.walk(USER_SPACE):
        # Filter out directories we don't want to copy
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
        
        # Calculate relative path to maintain folder structure
        rel_path = os.path.relpath(root, USER_SPACE)
        if rel_path == '.':
            dest_dir = export_path
        else:
            dest_dir = os.path.join(export_path, rel_path)
            os.makedirs(dest_dir, exist_ok=True)
            
        # Copy valid files
        for f in files:
            if f not in IGNORE_FILES and not f.startswith('.'):
                src_file = os.path.join(root, f)
                dst_file = os.path.join(dest_dir, f)
                shutil.copy2(src_file, dst_file)
                
    # Generate a clean Handoff README
    readme_content = f"""# {project_name}

> This project was compiled by the Omega Constitution on {datetime.now().strftime('%Y-%m-%d')}.

## Setup
(Insert your framework setup instructions here, e.g., `npm install`)

## Architecture
See the `02_architecture/` folder for system logic.
"""
    with open(os.path.join(export_path, "README.md"), 'w', encoding='utf-8') as format_readme:
        format_readme.write(readme_content)

def main():
    print("========================================")
    print("📦 OMEGA COMPILER: PROJECT HANDOFF")
    print("========================================")
    
    if not os.path.exists(USER_SPACE):
        print("❌ Error: USER SPACE folder not found. Nothing to compile.")
        return
        
    project_name = input("\nEnter the name of the final project (e.g., MyApp): ").strip()
    if not project_name:
        project_name = "Omega_Export"
        
    # Create valid directory name
    dir_name = "".join([c if c.isalnum() else "_" for c in project_name])
    export_path = os.path.join(DESKTOP_DIR, dir_name)
    
    if os.path.exists(export_path):
        print(f"\n⚠️ The folder '{dir_name}' already exists on your Desktop.")
        overwrite = input("Do you want to overwrite it? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("🛑 Compilation aborted.")
            return
        shutil.rmtree(export_path)
        
    print(f"\n🔨 Compiling '{project_name}'...")
    clean_copy_user_space(project_name, export_path)
    
    # Try to copy the handoff doc if it exists (assuming the AI placed it in root of USER SPACE)
    handoff_doc = os.path.join(USER_SPACE, "HANDOFF.md")
    if os.path.exists(handoff_doc):
        print("📄 Attaching AI HANDOFF.md architecture notes.")
        shutil.copy2(handoff_doc, os.path.join(export_path, "HANDOFF.md"))
        
    print(f"\n✅ SUCCESS! The project framework has been stripped away.")
    print(f"📂 Clean build exported to: {export_path}")

if __name__ == "__main__":
    main()
