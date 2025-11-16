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
