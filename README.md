# ❌⭕ Tic Tac Toe Game (Python)

## 📌 Description
This is a console-based Tic Tac Toe game built using Python. The project demonstrates modular programming by separating the game into multiple files.

It supports both:
- Multiplayer mode (Player vs Player)
- Single-player mode (Player vs Computer 🤖)

---

## 🎯 Features
- Two game modes:
  - Multiplayer
  - Single Player (Random AI)
- Turn-based gameplay
- Win detection (rows, columns, diagonals)
- Draw detection
- Input validation using try/except
- Score tracking system
- Replay functionality
- Clean terminal UI

---

## 📂 Project Structure

```
TicTacToe1.py   → Board Display
TicTacToe2.py   → Game Logic
TicTacToe3.py   → Main Game Controller
```

---

## 🧠 File-wise Explanation

### 📄 TicTacToe1.py (Board Display)
- Responsible for displaying the game board
- Uses list indexing to print a 3×3 grid

Example:
```python
display_board(board)
```

---

### 📄 TicTacToe2.py (Game Logic)
- Contains logic functions:
  - `check_winner()` → checks all winning conditions
  - `check_draw()` → checks if board is full

Example:
```python
check_winner(board, player)
check_draw(board)
```

---

### 📄 TicTacToe3.py (Main Program)
- Handles:
  - User input
  - Game flow
  - Mode selection
  - Player turns
  - Scoreboard
  - Computer moves (random)

---

## 🎮 Game Flow

1. Display position guide
2. Choose mode:
   - 1 → Multiplayer
   - 2 → Single Player
3. Enter player name(s)
4. Players take turns
5. System checks:
   - Winner
   - Draw
6. Score updates
7. Replay option

---

## 📍 Position Guide

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

---

## 🧠 Concepts Used
- Lists (for board representation)
- Functions (modular design)
- Loops (game flow)
- Conditional statements
- Exception handling
- Random module (computer moves)

---

## ⚙️ Technologies Used
- Python

---

## 🚀 Future Improvements
- Smart AI (block and win strategy)
- Difficulty levels
- GUI using Tkinter
- Highlight winning positions

---

## 👨‍💻 Author
Abhishek Raut
