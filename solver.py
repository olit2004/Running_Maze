import random

def get_moves(maze, r, c):
    res = []
    if r < maze.rows and maze.up[r][c] == 0:
        res.append((r + 1, c))
    if r > 1 and maze.up[r - 1][c] == 0:
        res.append((r - 1, c))
    if c > 1 and maze.right[r][c - 1] == 0:
        res.append((r, c - 1))
    if c < maze.cols and maze.right[r][c] == 0:
        res.append((r, c + 1))
    return res

def solve_step(maze):
    if maze.solved or not maze.built:
        return False

    if not maze.trace:
        maze.trace.append(maze.start)
        maze.visited.add(maze.start)
        maze.route = list(maze.trace)
        return True

    r, c = maze.trace[-1]

    if (r, c) == maze.end:
        maze.solved = True
        return False

    opts = get_moves(maze, r, c)
    new_opts = [m for m in opts if m not in maze.visited]

    if new_opts:
        nxt = random.choice(new_opts)
        maze.trace.append(nxt)
        maze.visited.add(nxt)
    else:
        maze.dead.add((r, c))
        maze.trace.pop()

    maze.route = list(maze.trace)
    
    if not maze.trace:
        return False

    return True