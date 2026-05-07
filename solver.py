import random


def get_possible_moves(maze, row, col):

    moves = []

    # UP
    if row > 0 and maze.northWall[row][col] == 0:
        moves.append((row - 1, col))

    # DOWN
    if row < maze.rows - 1 and maze.northWall[row + 1][col] == 0:
        moves.append((row + 1, col))

    # LEFT
    if col > 0 and maze.eastWall[row][col] == 0:
        moves.append((row, col - 1))

    # RIGHT
    if col < maze.cols - 1 and maze.eastWall[row][col + 1] == 0:
        moves.append((row, col + 1))

    return moves


def solve_maze(maze, start, end):

    stack = []

    visited = set()

    stack.append(start)

    visited.add(start)

    while stack:

        current = stack[-1]

        row, col = current

        # Save current path for rendering
        maze.solution_path = stack.copy()

        # Goal reached
        if current == end:
            return True

        possible_moves = get_possible_moves(
            maze,
            row,
            col
        )

        # Ignore already visited cells
        unvisited_moves = [
            move for move in possible_moves
            if move not in visited
        ]

        if unvisited_moves:

            next_move = random.choice(unvisited_moves)

            stack.append(next_move)

            visited.add(next_move)

        else:

            # Dead end
            maze.dead_ends.add(current)

            stack.pop()

    return False