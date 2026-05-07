from OpenGL.GL import *

CELL_SIZE = 0.08


def draw_cells(maze):

    # Draw dead-end cells (blue)
    glColor3f(0, 0, 1)

    for row, col in maze.dead_ends:

        x = -0.9 + col * CELL_SIZE
        y = 0.9 - row * CELL_SIZE

        glBegin(GL_QUADS)

        glVertex2f(x, y)
        glVertex2f(x + CELL_SIZE, y)

        glVertex2f(x + CELL_SIZE, y - CELL_SIZE)
        glVertex2f(x, y - CELL_SIZE)

        glEnd()

    # Draw solution path (red)
    glColor3f(1, 0, 0)

    for row, col in maze.solution_path:

        x = -0.9 + col * CELL_SIZE
        y = 0.9 - row * CELL_SIZE

        glBegin(GL_QUADS)

        glVertex2f(x, y)
        glVertex2f(x + CELL_SIZE, y)

        glVertex2f(x + CELL_SIZE, y - CELL_SIZE)
        glVertex2f(x, y - CELL_SIZE)

        glEnd()


def draw_grid(maze):

    rows = maze.rows
    cols = maze.cols

    glColor3f(1, 1, 1)

    # Horizontal walls
    for r in range(rows + 1):

        for c in range(cols):

            if maze.northWall[r][c]:

                x1 = -0.9 + c * CELL_SIZE
                y1 = 0.9 - r * CELL_SIZE

                x2 = x1 + CELL_SIZE
                y2 = y1

                glBegin(GL_LINES)

                glVertex2f(x1, y1)
                glVertex2f(x2, y2)

                glEnd()

    # Vertical walls
    for r in range(rows):

        for c in range(cols + 1):

            if maze.eastWall[r][c]:

                x1 = -0.9 + c * CELL_SIZE
                y1 = 0.9 - r * CELL_SIZE

                x2 = x1
                y2 = y1 - CELL_SIZE

                glBegin(GL_LINES)

                glVertex2f(x1, y1)
                glVertex2f(x2, y2)

                glEnd()