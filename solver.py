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

def solve_step(maze, algo="DFS"):
    if maze.solved or not maze.built:
        return False
    
    if algo == "BFS":
        return bfs_step(maze)
    else:
        return dfs_step(maze)

def dfs_step(maze):
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

def bfs_step(maze):
    if not maze.queue:
        maze.queue.append(maze.start)
        maze.visited.add(maze.start)
        maze.parents[maze.start] = None
        return True

    curr = maze.queue.pop(0)
    maze.dead.add(curr) # Use dead for all visited cells in BFS visualization

    if curr == maze.end:
        maze.solved = True
        # Reconstruct path
        path = []
        temp = curr
        while temp:
            path.append(temp)
            temp = maze.parents[temp]
        maze.route = path[::-1]
        return False

    opts = get_moves(maze, curr[0], curr[1])
    for nxt in opts:
        if nxt not in maze.visited:
            maze.visited.add(nxt)
            maze.parents[nxt] = curr
            maze.queue.append(nxt)

    # For visualization during BFS, we can show the path to the current node
    path = []
    temp = curr
    while temp:
        path.append(temp)
        temp = maze.parents[temp]
    maze.route = path[::-1]

    if not maze.queue:
        return False

    return True