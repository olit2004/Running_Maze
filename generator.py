import random


def get_unvisited_neighbors(maze, row, col):

    neighbors = []

    # UP
    if row > 0 and not maze.visited[row - 1][col]:
        neighbors.append(("UP", row - 1, col))

    # DOWN
    if row < maze.rows - 1 and not maze.visited[row + 1][col]:
        neighbors.append(("DOWN", row + 1, col))

    # LEFT
    if col > 0 and not maze.visited[row][col - 1]:
        neighbors.append(("LEFT", row, col - 1))

    # RIGHT
    if col < maze.cols - 1 and not maze.visited[row][col + 1]:
        neighbors.append(("RIGHT", row, col + 1))

    return neighbors


def remove_wall(
    maze,
    current_row,
    current_col,
    next_row,
    next_col,
    direction
):

    # Remove top wall
    if direction == "UP":
        maze.northWall[current_row][current_col] = 0

    # Remove bottom wall
    elif direction == "DOWN":
        maze.northWall[current_row + 1][current_col] = 0

    # Remove left wall
    elif direction == "LEFT":
        maze.eastWall[current_row][current_col] = 0

    # Remove right wall
    elif direction == "RIGHT":
        maze.eastWall[current_row][current_col + 1] = 0


def generate_maze(maze):

    stack = []

    # Random starting cell
    current_row = random.randint(0, maze.rows - 1)
    current_col = random.randint(0, maze.cols - 1)

    maze.visited[current_row][current_col] = True

    while True:

        neighbors = get_unvisited_neighbors(
            maze,
            current_row,
            current_col
        )

        if neighbors:

            # Save position for backtracking
            stack.append((current_row, current_col))

            # Pick random neighbor
            direction, next_row, next_col = random.choice(neighbors)

            # Remove wall between current and next
            remove_wall(
                maze,
                current_row,
                current_col,
                next_row,
                next_col,
                direction
            )

            # Move to next cell
            current_row = next_row
            current_col = next_col

            maze.visited[current_row][current_col] = True

        elif stack:

            # Backtrack
            current_row, current_col = stack.pop()

        else:

            # Finished
            break


def create_entrance_and_exit(maze):

    # Entrance (left boundary)
    start_row = random.randint(0, maze.rows - 1)
    maze.eastWall[start_row][0] = 0

    # Exit (right boundary)
    end_row = random.randint(0, maze.rows - 1)
    maze.eastWall[end_row][maze.cols] = 0

    return (start_row, 0), (end_row, maze.cols - 1)