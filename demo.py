import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from maze import Maze
from renderer import draw
from generator import gen_step, place_points

# Settings
rows, cols = 10, 10
size = 1.8 / max(rows, cols)
speed = 40
maze = Maze(rows, cols)

def tick(val):
    if not maze.built:
        if not gen_step(maze):
            place_points(maze)
            print("\n--- Maze Code Generated! ---")
            print(f"up = {maze.up}")
            print(f"right = {maze.right}")
            print(f"start = {maze.start}")
            print(f"end = {maze.end}")
            print("--- Copy-paste the above into a script to reconstruct this maze ---")
    
    glutPostRedisplay()
    glutTimerFunc(speed, tick, 0)

def show():
    glClear(GL_COLOR_BUFFER_BIT)
    draw(maze, size)
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"Dynamic Maze Generator")
    
    glClearColor(0, 0, 0, 1)
    glutDisplayFunc(show)
    glutTimerFunc(speed, tick, 0)
    
    print("Running generation demo...")
    print("When finished, the maze data will be printed as code in this terminal.")
    glutMainLoop()

if __name__ == "__main__":
    main()
