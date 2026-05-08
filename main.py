import sys
from OpenGL.GL import *
from OpenGL.GLUT import *

from maze import Maze
from renderer import draw
from generator import gen_step, place_points
from solver import solve_step

# Configuration
ROWS = 15
COLS = 15
CELL_SIZE = 1.8 / max(ROWS, COLS)
ANIMATION_SPEED = 50 # ms delay

maze = Maze(ROWS, COLS)
state = "GENERATING" # GENERATING, READY_TO_SOLVE, SOLVING, FINISHED

def update(value):
    global state
    
    if state == "GENERATING":
        if not gen_step(maze):
            place_points(maze)
            state = "READY_TO_SOLVE"
           
            glutTimerFunc(2000, lambda v: start_solving(), 0)
    
    elif state == "SOLVING":
        if not solve_step(maze):
            state = "FINISHED"

    glutPostRedisplay()
    glutTimerFunc(ANIMATION_SPEED, update, 0)

def start_solving():
    global state
    if state == "READY_TO_SOLVE":
        state = "SOLVING"

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw(maze, CELL_SIZE)
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Maze Generator & Solver - Graphics Assignment")
    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    glutDisplayFunc(display)
    glutTimerFunc(ANIMATION_SPEED, update, 0)
    

    
    glutMainLoop()

if __name__ == "__main__":
    main()