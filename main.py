import os
import platform
import shutil
import sys
from datetime import datetime
from pathlib import Path


def prompt_path(label: str) -> Path:
    """Keep asking until the user supplies an existing path."""
    while True:
        p = Path(os.path.expanduser(input(label).strip())).resolve()
        if p.exists():
            return p
        print(f"'{p}' does not exist. Try again.\n")


def main() -> None:
    # OS guard
    if platform.system() != "Linux":
        input(
            "Warning: script is intended for Linux. Press Enter to continue "
            "anyway, or Ctrl‑C to abort."
        )

    # Collect paths
    linux_path = prompt_path("Enter the full path to the existing LINUX save folder: ")
    win_path = prompt_path("Enter the full path to the WINDOWS save folder: ")

    if win_path.samefile(linux_path):
        print("The two paths are identical – nothing to do.")
        return

    # Confirm
    input(
        "\nThe Linux save folder will be MOVED to Trash and replaced with a "
        "symlink pointing at the Windows path.\nPress Enter to continue or "
        "Ctrl‑C to abort.\n"
    )

    # Prepare Trash
    script_dir = Path(__file__).resolve().parent
    trash_root = script_dir / "Trash"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    trash_target = trash_root / timestamp
    trash_target.mkdir(parents=True, exist_ok=True)  # creates Trash if absent

    # Move Linux files
    moved_dest = trash_target / linux_path.name
    print(f"Moving '{linux_path}'  →  '{moved_dest}'")
    shutil.move(str(linux_path), moved_dest)

    # Create symlink
    print(f"Creating symlink '{linux_path}'  →  '{win_path}'")
    os.symlink(src=win_path, dst=linux_path)

    print("\nDone. Verify the new link before launching any game.")


if __name__ == "__main__":
    main()