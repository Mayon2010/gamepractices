# Read Me for Game Projects

---

## Legends of Avalor (APCSP Project 1)

An interactive text-based adventure game that strengthens core Python skills in **if-else statements** and **decision-making logic**. Players embark on an epic quest to rescue the Princess of Avalor from the clutches of the evil Vader Dark, with each decision branching into new storylines.

### Features
- **Multiple Storylines**: Over 14 unique scenes with branching narratives
- **Interactive Decision System**: Player choices directly impact the story outcome
- **If-Else Logic Implementation**: Demonstrates fundamental conditional programming
- **Win/Lose Conditions**: Multiple endings based on strategic choices
- **Engaging Narrative**: Fantasy-themed adventure with characters and plot twists
- **Turn-Based Choices**: Sequential decision-making gameplay

### How to Play
1. Run the script using Python 3:
   ```powershell
   python apcsp-project1.py
   ```
2. The game will introduce you to the world of Avalor and explain your quest.
3. At each scene, you'll be presented with 2-3 choices (numbered 1, 2, or 3).
4. Enter the number corresponding to your choice when prompted.
5. Your decisions will determine which scenes you visit and how the story progresses.
6. Reach a **winning ending** by making the right choices, or trigger a **game over** if you choose poorly.

### Game Story Overview
You awaken in your home to learn that the Princess of Avalor has been abducted by Vader Dark and imprisoned in the Vermillion Temple. As the chosen hero, you must:

1. **Leave Your Home** - Decide whether to begin your quest or ignore the call to adventure
2. **Gather Supplies & Wisdom** - Find the mysterious old man who reveals the location of the Sword of Life
3. **Obtain the Legendary Weapon** - Defeat a spirit warrior to claim the Sword of Life from the enchanted meadow
4. **Reach the Temple** - Navigate through treacherous terrain and make moral choices that define your character
5. **Face Vader Dark** - Engage in a final battle using courage and the legendary sword to save the kingdom

### Scene Map & Decision Flow
```
Scene 1: Wake Up Decision
├─ Choice 1 → Scene 2: Explore the World
│  ├─ Choice 1 → Scene 6: Visit Old Man's House
│  │  ├─ Choice 1 → Game Over (ignored advice)
│  │  └─ Choice 2 → Scene 7: Journey to Meadow
│  │     ├─ Choice 1 → Scene 9: Direct Path to Temple
│  │     │  ├─ Choice 1 → Scene 12: Duel with Vader Dark
│  │     │  │  └─ Choice 1 → Scene 14: Victory! (Good Ending)
│  │     │  └─ Choice 2/3 → Game Over (Lost)
│  │     ├─ Choice 2 → Game Over (Went Home)
│  │     └─ Choice 3 → Scene 8: Save Old Man
│  │        └─ Choice 1 → Scene 10: Portal to Temple
│  │           └─ Choice 1 → Scene 11: Battle
│  │              └─ Choice 1 → Scene 13: Victory! (Good Ending)
│  └─ Choice 2/3 → Game Over (Wrong Path)
├─ Choice 2 → Scene 3: Game Over (Fell Asleep)
└─ Choice 3 → Scene 4: Game Over (Debated with Friend)
```

### Key Concepts Taught
This project demonstrates essential Python programming concepts:

| Concept | Example |
|---------|---------|
| **If-Else Statements** | Checking if player choice == 1, 2, or 3 |
| **Nested Conditionals** | Multiple levels of if-else to handle story branching |
| **Functions** | Each scene is a function that returns player choice |
| **User Input** | `int(input())` to collect player decisions |
| **Variable Assignment** | Storing choices in variables for conditional checking |
| **Control Flow** | Using choice variables to navigate story paths |

### Winning Endings
There are **2 main winning endings**:

1. **Good Ending 1**: Follow the old man's advice → Travel directly to temple → Defeat Vader Dark
2. **Good Ending 2**: Show compassion → Save the old man → Use the portal → Defeat Vader Dark

Both endings result in the princess being saved and the kingdom of Avalor being freed from darkness.

### Losing Conditions
The game ends in failure if you:
- Ignore the initial call to adventure (sleep or debate)
- Refuse the old man's guidance
- Turn back from your quest (choose to go home)
- Lose courage when facing Vader Dark (run away or accept defeat)
- Make invalid input choices (enter numbers other than 1, 2, or 3)

### File Structure
- `apcsp-project1.py`: Main script containing all 14 scenes and game logic

### Requirements
- Python 3.x
- No external dependencies

### Educational Objectives
By playing and studying this code, students will understand:
- How if-else statements create branching logic
- How functions organize complex code
- How variables store and retrieve player choices
- The relationship between input, conditional logic, and output
- How nested conditions handle complex decision trees

### License
This project is provided for educational purposes and is released under the MIT License.

---

# Chess Game 1 (Console Version)

This is a simple console-based chess game implemented in Python. It allows two players to play chess by entering moves in algebraic notation. The game enforces basic move legality for all standard chess pieces.

## Features
- Full 8x8 chess board representation
- All standard chess pieces: King, Queen, Rook, Bishop, Knight, Pawn
- Move validation for each piece according to chess rules
- Pawn double-step on first move and diagonal captures
- Console-based board display with piece symbols
- Turn-based play for White and Black
- Simple move input (e.g., `e2e4`)
- Exit option to quit the game

## How to Play
1. Run the script using Python 3:
   ```powershell
   python chessvers2.py
   ```
2. The board will be displayed in the console. White moves first.
3. Enter moves in the format: `<from><to>`, e.g., `e2e4` moves the piece from e2 to e4.
4. The game checks for move legality and enforces turn order.
5. Type `exit` to quit the game at any time.

## Board Display
- Rows are numbered 8 (top) to 1 (bottom).
- Columns are labeled a-h (left to right).
- Piece symbols:
  - Uppercase: White pieces (K, Q, R, B, N, P)
  - Lowercase: Black pieces (k, q, r, b, n, p)
  - `.`: Empty square

Example:
```
8 r n b q k b n r 
7 p p p p p p p p 
6 . . . . . . . . 
5 . . . . . . . . 
4 . . . . . . . . 
3 . . . . . . . . 
2 P P P P P P P P 
1 R N B Q K B N R 
  a b c d e f g h
```

## Limitations
- No check/checkmate detection
- No castling, en passant, or pawn promotion
- No AI; only two-player mode
- No move history or undo

## File Structure
- `chessvers2.py`: Main script containing all game logic and piece definitions

## Requirements
- Python 3.x
- No external dependencies

## License
This project is provided for educational purposes and is released under the MIT License.

# Notes App — `notestest.py`

A small desktop Notes application written in Python using Tkinter. It provides a simple UI to create, edit, delete, export, and organize plain-text notes into folders. This README documents the app, how to run it, the supporting scripts and folders (`notes/`, `notesassets/`, and `generate_notesassets.py`), and troubleshooting tips.

---

## Overview

- **Primary script**: `notestest.py` — Tkinter-based GUI application (single-file, minimal dependencies).
- **Assets folder**: `notesassets/` — contains small PNG icons used by the UI.
- **Notes storage**: `notes/` — a folder containing subfolders (e.g., `General/`) with `.txt` note files.
- **Helper script**: `generate_notesassets.py` — generates placeholder PNG icons (requires Pillow).

The app uses only the Python standard library (Tkinter) for runtime UI; the icon generator uses Pillow if you want to create/update icons.

## Features

- Create new plain-text notes and save them into named folders.
- Browse existing folders and notes.
- Edit, save, delete, and export notes to arbitrary file paths.
- Lightweight icon support — if `notesassets/` contains PNG icons the UI will load them; missing icons fall back to text-only buttons.
- Automatic creation of a default `General` folder when none exist.

## Requirements

- Python 3.7+ (Tkinter included with standard Python installations on Windows/macOS/Linux).
- Optional: `Pillow` (PIL) to run `generate_notesassets.py`.

Install Pillow (optional) using PowerShell on Windows:

```powershell
python -m pip install --upgrade pip
python -m pip install pillow
```

## Folder Structure

- `notestest.py` — main application.
- `generate_notesassets.py` — script to generate placeholder icons (uses Pillow).
- `notes/` — runtime folder where note subfolders and `.txt` files are stored. Example layout:
  - `notes/General/*.txt`
  - `notes/testing/test2.txt`
- `notesassets/` — icon files used by the UI (e.g., `create.png`, `open.png`, `save.png`, etc.).

The repository currently includes example assets in `notesassets/` and example content under `notes/General` and `notes/testing/`.

## Running the App

Run the application from the project root (the same folder that contains `notestest.py`). Example PowerShell command:

```powershell
python notestest.py
```

Behavior on first run:

- The app will create a `notes/` directory (if it doesn't exist) and ensure a `General` folder exists.
- If `notesassets/` contains PNG files named like `create.png`, `open.png`, etc., the UI will use them; otherwise the app will display text-only buttons.

## generate_notesassets.py — Create placeholder icons

`generate_notesassets.py` creates simple 32x32 PNG icons into `notesassets/` for use by the UI. Usage:

```powershell
python generate_notesassets.py
```

- Requires `Pillow` (`pip install pillow`).
- The script writes several files such as `create.png`, `open.png`, `save.png`, `back.png`, etc.
- These are intentionally simple placeholders and work well for prototyping.

## Notes App Behavior & UX

- Creating a note: choose a name, select an existing folder or choose "New Folder" and provide a folder name. The note content is saved as a `.txt` file in the chosen folder.
- Opening notes: the app lists folders from `notes/` and displays `.txt` notes in the selected folder.
- Editing notes: save writes changes back to the existing `.txt` file.
- Deleting notes: removes the `.txt` file from disk (confirmation dialog shown).
- Exporting notes: saves a copy to a user-selected path via a Save dialog.

## Example Walkthrough (Windows PowerShell)

1. Generate icons (optional):

```powershell
python generate_notesassets.py
```

2. Start the Notes App:

```powershell
python notestest.py
```

3. Create a new note, save it in `General`, then open and export it via the UI.

## Troubleshooting

- If the UI shows text-only buttons, confirm that `notesassets/` contains the named PNG files: `create.png`, `open.png`, `exit.png`, `save_note.png`, `save.png`, `back.png`, `folder.png`, `note.png`, `delete.png`, `export.png`.
- If icons fail to load and you want a clean regeneration, install `Pillow` and run `generate_notesassets.py`.
- On file write errors, ensure you have write permissions to the project directory and that no other program is locking the file.
- If Tkinter is not available on your Python install, install a standard CPython distribution or ensure the `python` you run includes Tkinter (on some Linux distributions you may need `sudo apt install python3-tk`).

## Security & Data Considerations

- Notes are stored as plain text (`.txt`) with no encryption. Do not store secrets in these files.
- Deletion is permanent (file is removed from disk). Consider manually backing up the `notes/` folder.

## Contributing & Improvements

If you want to improve the app, suggested enhancements:

- Add search across notes and folders.
- Add optional encryption or password-protection for private notes.
- Add note metadata (created/modified timestamps) and show them in the UI.
- Add import/export in other formats (Markdown, JSON) and batch operations.
- Add unit tests for helper functions (folder and note listing) and automation scripts.

To propose changes:

1. Fork the repo and create a feature branch.
2. Open a pull request with a clear description of changes and rationale.

## License

This application and supporting scripts are provided for educational purposes. Unless otherwise specified in repository metadata, treat the code as available under the MIT license for personal and educational use.

---

# Other Projects

This repository also contains other projects (games and experiments). See the older sections below for details on those projects. The Notes App documentation above is the recommended starting point if you're exploring the `notestest.py` functionality and related assets.

<!-- End of file -->
```