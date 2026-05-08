from maze import Maze
from solver import bfs_step

def test_bfs():
    m = Maze(5, 5)
    # Mock a simple maze path from (1,1) to (5,5)
    m.built = True
    m.start = (1, 1)
    m.end = (5, 5)
    
    # Connect (1,1) -> (1,2) -> (1,3) -> (1,4) -> (1,5) -> (2,5) -> ... -> (5,5)
    for c in range(1, 5):
        m.right[1][c] = 0
    for r in range(1, 5):
        m.up[r][5] = 0
    
    print(f"Start: {m.start}, End: {m.end}")
    
    steps = 0
    while not m.solved and steps < 100:
        res = bfs_step(m)
        steps += 1
        if not res:
            print(f"BFS stopped after {steps} steps. Solved: {m.solved}")
            break
        if m.solved:
            print(f"BFS solved in {steps} steps!")
            print(f"Path: {m.route}")
            break
    else:
        if not m.solved:
            print("BFS failed to solve in 100 steps.")

if __name__ == "__main__":
    test_bfs()
