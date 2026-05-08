#  Interactive Maze Lab

A visually rich, real-time maze generation and solving simulation built with **Python** and **OpenGL**. 

<p align="center">
  <a href="https://www.loom.com/share/cde54a5bca7946d3ae7080b6b2bb1b86" style="color:blue; font-size:24px; font-weight:bold;">
    ▶ Loom Demo Video
  </a>
</p>




This application is **fully interactive**: users can customize the maze dimensions (any number of rows and columns) and choose between different solving algorithms like **BFS** and **DFS** to compare their performance and behavior in real-time.

---

##  Features

- **Dynamic Generation**: Watch the "mouse" carve out a unique maze using randomized DFS.
- **Dual Solving Algorithms**: Choose between two fundamental search strategies:
  - **DFS (Depth-First Search)**: Follows a single path to its end, backtracking only when necessary.
  - **BFS (Breadth-First Search)**: Explores all neighbors simultaneously, guaranteeing the shortest path.
- **Interactive UI**: Customize maze dimensions (Rows/Cols) and toggle algorithms .
- **Real-time Visualization**: See the algorithms work step-by-step with color-coded paths.

---

## How it Works

### 1. Maze Generation
The maze is generated using a **stack-based randomized Depth-First Search** (Recursive Backtracking):
- The generator starts at a random cell and carves through walls to reach unvisited neighbors.
- If it hits a dead end, it backtracks using a stack until it finds a cell with unvisited neighbors.
- **Result**: A "Perfect Maze" (no loops and exactly one path between any two points).

### 2. Solving Algorithms
- **DFS (Depth-First Search)**:
  - Explores as deep as possible along each branch before backtracking.
  - Represented by a single red line showing the current stack.
- **BFS (Breadth-First Search)**:
  - Explores all cells at the current depth before moving to the next level.
  - Represented by a blue "flood fill" of visited nodes and a red path showing the shortest route to the frontier.



##  Technical Details

- **Language**: Python 3.x
- **Graphics**: PyOpenGL (OpenGL 2.1 compatible)
- **UI Architecture**: Custom manual UI rendering within the OpenGL context.
- **Algorithms**: 
  - Randomized DFS (Backtracking) for generation.
  - Stack-based DFS for solving.
  - Queue-based BFS with parent tracking for shortest path solving.

---

## Installation & Running

### Prerequisites
Ensure you have the OpenGL libraries installed:
```bash
pip install PyOpenGL PyOpenGL_accelerate
```

### Run the Lab
```bash
python main.py
```

---

##  Visualization Guide
- 🟥 **Red Cells**: The current path being explored.
- 🟦 **Blue Cells**: Visited nodes / Dead ends.
- 🟩 **Green Cell**: Starting point.
- 🟪 **Magenta Cell**: Exit point.
- 🟨 **Yellow Cell**: Generator's current position.
