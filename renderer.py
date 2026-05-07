from OpenGL.GL import *

CELL_SIZE = 0.08

def draw_grid(maze):
    rows = maze.rows
    cols = maze.cols

    glColor3f(1, 1, 1)

   
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