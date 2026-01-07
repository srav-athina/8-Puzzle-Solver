# 8-Puzzle Solver 🧩

![Status](https://img.shields.io/badge/Status-Archived-red)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Course](https://img.shields.io/badge/Course-Analysis_of_Algorithms-green)

> **Note:** This project is archived and no longer actively maintained. It serves as a reference implementation for solving sliding window puzzles using heuristic search algorithms.

## 📖 Overview
This project is a Python implementation of an automated solver for the **8-Puzzle** (sliding tile puzzle). It utilizes fundamental AI search algorithms to find the optimal path from a scrambled state to the goal state.

The core focus of this project was to compare the efficiency of uninformed search strategies (BFS) against informed heuristic searches (A*) in terms of **time complexity** and **memory usage**.

## 🧠 Algorithms Implemented
* **A* Search (A-Star):** Uses heuristics to find the shortest path to the solution.
    * *Heuristic 1:* **Manhattan Distance** (Sum of vertical/horizontal distances).
    * *Heuristic 2:* **Euclidean Distance** (Straight-line distance).
* **Breadth-First Search (BFS):** Explores all neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

## ⚙️ How It Works
The solver represents the puzzle board as a 3x3 matrix (or linear array). It generates a "game tree" where each node is a valid board state.
1.  **Input:** User provides an initial scrambled state (e.g., `1 0 3 4 2 5 7 8 6`).
2.  **Processing:** The algorithm explores states, calculating the cost `f(n) = g(n) + h(n)` for A*.
3.  **Output:** Prints the sequence of moves (Up, Down, Left, Right) to solve the puzzle.

## 🚀 Usage

### Prerequisites
* Python 3.x

### Running the Solver
```bash
# Clone the repository
git clone [https://github.com/srav-athina/8-Puzzle-Solver.git](https://github.com/srav-athina/8-Puzzle-Solver.git)

# Navigate to directory
cd 8-Puzzle-Solver

# Run the solver
python solver.py
