from OpenGL.GL import *
from OpenGL.GLUT import *

from maze import Maze

from renderer import draw_grid, draw_cells

from generator import (
    generate_maze,
    create_entrance_and_exit
)

from solver import solve_maze


maze = Maze(10, 10)

# Generate maze
generate_maze(maze)

# Create entrance and exit
start, end = create_entrance_and_exit(maze)

# Solve maze
solve_maze(maze, start, end)


def display():

    glClear(GL_COLOR_BUFFER_BIT)

    # Draw colored cells first
    draw_cells(maze)

    # Draw walls on top
    draw_grid(maze)

    glFlush()


glutInit()

glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

glutInitWindowSize(800, 800)

glutCreateWindow(b"Maze Generator and Solver")

glClearColor(0, 0, 0, 1)

glutDisplayFunc(display)

glutMainLoop()