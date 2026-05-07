from OpenGL.GL import *
from OpenGL.GLUT import *

from maze import Maze
from renderer import draw_grid

maze = Maze(10, 10)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    draw_grid(maze)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 800)

glutCreateWindow(b"Maze")

glClearColor(0, 0, 0, 1)

glutDisplayFunc(display)

glutMainLoop()