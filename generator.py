import random

def get_neighbors(maze, r, c):
    res = []
    if r < maze.rows and not maze.seen[r + 1][c]:
        res.append(("UP", r + 1, c))
    if r > 1 and not maze.seen[r - 1][c]:
        res.append(("DOWN", r - 1, c))
    if c > 1 and not maze.seen[r][c - 1]:
        res.append(("LEFT", r, c - 1))
    if c < maze.cols and not maze.seen[r][c + 1]:
        res.append(("RIGHT", r, c + 1))
    return res

def cut(maze, r, c, dir):
    if dir == "UP":
        maze.up[r][c] = 0
    elif dir == "DOWN":
        maze.up[r - 1][c] = 0
    elif dir == "LEFT":
        maze.right[r][c - 1] = 0
    elif dir == "RIGHT":
        maze.right[r][c] = 0

def gen_step(maze):
    if maze.built:
        return False

    if maze.curr is None:
        maze.curr = (random.randint(1, maze.rows), random.randint(1, maze.cols))
        maze.seen[maze.curr[0]][maze.curr[1]] = True
        return True

    r, c = maze.curr
    nbs = get_neighbors(maze, r, c)

    if nbs:
        maze.stack.append((r, c))
        dir, nr, nc = random.choice(nbs)
        cut(maze, r, c, dir)
        maze.curr = (nr, nc)
        maze.seen[nr][nc] = True
    elif maze.stack:
        maze.curr = maze.stack.pop()
    else:
        maze.built = True
        loops(maze)
        return False
    
    return True

def loops(maze):
    for r in range(1, maze.rows + 1):
        for c in range(1, maze.cols + 1):
            if random.random() < 0.05:
                w = random.choice(["N", "E"])
                if w == "N" and r < maze.rows:
                    maze.up[r][c] = 0
                elif w == "E" and c < maze.cols:
                    maze.right[r][c] = 0

def place_points(maze):
    if maze.rows > 2 and maze.cols > 2:
        maze.start = (random.randint(2, maze.rows - 1), random.randint(2, maze.cols - 1))
        maze.end = (random.randint(2, maze.rows - 1), random.randint(2, maze.cols - 1))
        while maze.end == maze.start:
            maze.end = (random.randint(2, maze.rows - 1), random.randint(2, maze.cols - 1))
    else:
        maze.start = (1, 1)
        maze.end = (maze.rows, maze.cols)