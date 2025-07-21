# Permanent Save Syncer

A simple Python utility to automate cross-platform game save syncing for dual-boot setups (Linux + Windows).  
**Safely replaces any Linux game save folder with a symlink to its Windows counterpart, archiving your original Linux save in a dated Trash folder for easy recovery.**

---

## Why?

Many PC games—especially those outside Steam, or games launched via Proton/Epic/Heroic—don’t sync saves between Windows and Linux by default. This script removes the hassle:  
- No more manual copying or risk of overwriting the wrong save.  
- Easily reverse the process: all original data is moved to a dated Trash folder before any changes are made.

---

## Features

- **Cross-platform sanity:** Refuses to run on Windows (unless you force override), because symlink semantics differ.
- **Safety-first:** Moves your original Linux save folder to a local `Trash` directory with a timestamp, not outright deletion.
- **Symlink automagic:** Replaces your Linux save path with a symlink pointing directly to your Windows save, letting your games on Linux read/write seamlessly to the same files.

---

## Usage

1. **Requirements:**  
   - Python 3.7+
   - Linux OS (for intended behavior; see [FAQ](#faq) below for Windows)
2. **Clone or download this repo.**
3. **Open a terminal and run:**
   ```bash
   python main.py
   ```
4. **Follow the prompts:**

   * Enter the path to your existing Linux save folder (e.g., `~/.local/share/GameName/saves`)
   * Enter the path to your Windows save folder (on your mounted NTFS partition, e.g., `/mnt/windows/Users/YourName/Documents/GameName/Saves`)
   * Confirm before any data is moved.
5. **Result:**

   * Your Linux save folder is safely moved to `Trash/YYYY-MM-DD_HH-MM-SS` in the same directory as the script.
   * A symlink is created at the old Linux save path, pointing to your Windows save folder.

---

## Example

```shell
$ python main.py
Enter the full path to the existing LINUX save folder: ~/.local/share/Hades
Enter the full path to the WINDOWS save folder: /mnt/windows/Users/sushi/Documents/Hades
(The Linux save folder will be MOVED to Trash and replaced with a symlink...)
Moving '/home/sushi/.local/share/Hades' → '/home/sushi/SyncSaveLinker/Trash/2025-07-21_13-52-16/Hades'
Creating symlink '/home/sushi/.local/share/Hades' → '/mnt/windows/Users/sushi/Documents/Hades'
Done. Verify the new link before launching any game.
```

---

## FAQ

**Q: Why not run this on Windows?**
A: This script is designed for Linux. Windows’ symlinks behave differently and require admin rights. If you want bidirectional sync or Windows support, open an issue or PR.

**Q: What happens if I make a mistake?**
A: Your original Linux save is not deleted. Check the `Trash` folder next to the script for all backups.

**Q: Can I use this for files (not just folders)?**
A: Yes, works with both files and folders.

**Q: Do I need to run this every time?**
A: No. Once set up, your saves are always synced via the symlink—unless you move or break the link.

---

## Contributing

Pull requests, feature suggestions, and bug reports are welcome.

---
