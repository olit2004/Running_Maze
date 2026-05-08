# Maze Generator and Solver

This project implements a rectangular maze generator and solver using OpenGL for visualization. 

## How it Works

### 1. Maze Generation (The "Mouse")
The maze is generated using a **stack-based Depth First Search (DFS)** algorithm, often called "Recursive Backtracking":
- An invisible "mouse" starts at a random cell and "eats" through walls to connect to unvisited neighbors.
- If the mouse hits a dead end, it pops the stack to return to the last cell with unvisited neighbors.
- This ensures a **proper maze**: every cell is connected by a unique path.

### 2. Maze Solving
The solver uses a similar **backtracking algorithm**:
- The mouse tries to move in random valid directions (where there is no wall).
- It keeps track of its current path on a stack (**Red dots**).
- When it hits a dead end, it marks the cell as a dead end (**Blue dots**) and backtracks by popping the stack.
- The process continues until the end cell is reached.

## Technical Details


## How to Run
Ensure you have `PyOpenGL` installed:
```bash
pip install PyOpenGL PyOpenGL_accelerate
```
Run the main script:
```bash
python main.py
```
