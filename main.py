import sys
from OpenGL.GL import *
from OpenGL.GLUT import *

from maze import Maze
from renderer import draw
from generator import gen_step, place_points
from solver import solve_step

ANIMATION_SPEED = 30  
DEFAULT_ROWS = 15
DEFAULT_COLS = 15

maze = Maze(DEFAULT_ROWS, DEFAULT_COLS)
ui_state = {
    'rows_text': str(DEFAULT_ROWS),
    'cols_text': str(DEFAULT_COLS),
    'focus': None,
    'state': 'IDLE',
    'algo': 'DFS'
}

def update(value):
    if ui_state['state'] == "GENERATING":
        if not gen_step(maze):
            place_points(maze)
            ui_state['state'] = "READY_TO_SOLVE"
    
    elif ui_state['state'] == "SOLVING":
        if not solve_step(maze, ui_state['algo']):
            ui_state['state'] = "FINISHED"

    glutPostRedisplay()
    glutTimerFunc(ANIMATION_SPEED, update, 0)

def reset_maze():
    global maze
    try:
        r = int(ui_state['rows_text'])
        c = int(ui_state['cols_text'])
        if r < 1 or c < 1: return
        maze = Maze(r, c)
        ui_state['state'] = "GENERATING"
    except ValueError:
        pass

def start_solving():
    if ui_state['state'] == "READY_TO_SOLVE":
        ui_state['state'] = "SOLVING"

def mouse_handler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        nx = (x / 800.0) * 2 - 1
        ny = 1 - (y / 800.0) * 2
        
        if -0.9 <= nx <= -0.5 and 0.52 <= ny <= 0.6:
            ui_state['focus'] = 'rows'
        elif -0.9 <= nx <= -0.5 and 0.32 <= ny <= 0.4:
            ui_state['focus'] = 'cols'
        elif -0.9 <= nx <= -0.5 and 0.1 <= ny <= 0.22:
            reset_maze()
            ui_state['focus'] = None
        
        elif -0.9 <= nx <= -0.5 and -0.1 <= ny <= 0.02:
            start_solving()
            ui_state['focus'] = None
        
        # Algo selection
        elif -0.9 <= nx <= -0.72 and -0.3 <= ny <= -0.22:
            ui_state['algo'] = 'DFS'
        elif -0.68 <= nx <= -0.5 and -0.3 <= ny <= -0.22:
            ui_state['algo'] = 'BFS'
            
        else:
            ui_state['focus'] = None
        
        glutPostRedisplay()

def keyboard_handler(key, x, y):
    focus = ui_state['focus']
    if focus:
        
        if key == b'\x08':
            ui_state[focus + '_text'] = ui_state[focus + '_text'][:-1]
        elif key == b'\r': 
            ui_state['focus'] = None
        else:
            try:
                char = key.decode('utf-8')
                if char.isdigit():
                    if len(ui_state[focus + '_text']) < 3:
                        ui_state[focus + '_text'] += char
            except:
                pass
    
    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw UI
    from renderer import draw_ui
    draw_ui(ui_state)
    
    # Draw Maze
    cell_size = 1.2 / max(maze.rows, maze.cols)
    draw(maze, cell_size)
    
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Olit's Maze - Graphics Assignment")
    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    glutDisplayFunc(display)
    glutMouseFunc(mouse_handler)
    glutKeyboardFunc(keyboard_handler)
    glutTimerFunc(ANIMATION_SPEED, update, 0)
    
    glutMainLoop()

if __name__ == "__main__":
    main()