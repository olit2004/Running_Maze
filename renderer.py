from OpenGL.GL import *
from OpenGL.GLUT import *

def draw(maze, size):
    ox = -0.3
    oy = -0.9

    glColor3f(0.0, 0.0, 1.0)
    for r, c in maze.dead:
        box(r, c, size, ox, oy)
    
    glColor3f(1.0, 0.0, 0.0)
    for r, c in maze.route:
        box(r, c, size, ox, oy)
    
    if maze.start:
        glColor3f(0.0, 1.0, 0.0)
        box(maze.start[0], maze.start[1], size, ox, oy)
    if maze.end:
        glColor3f(1.0, 0.0, 1.0)
        box(maze.end[0], maze.end[1], size, ox, oy)
    
    if maze.curr and not maze.built:
        glColor3f(1.0, 1.0, 0.0)
        box(maze.curr[0], maze.curr[1], size, ox, oy)

    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    
    for r in range(0, maze.rows + 1):
        for c in range(0, maze.cols + 1):
            x = ox + (c - 1) * size
            y = oy + (r - 1) * size
            
            if r <= maze.rows and c >= 1 and maze.up[r][c]:
                glVertex2f(x, y + size)
                glVertex2f(x + size, y + size)
            
            if c <= maze.cols and r >= 1 and maze.right[r][c]:
                glVertex2f(x + size, y)
                glVertex2f(x + size, y + size)
                
            if r == 0 and c >= 1 and maze.up[0][c]:
                glVertex2f(x, y + size)
                glVertex2f(x + size, y + size)
            
            if c == 0 and r >= 1 and maze.right[r][0]:
                glVertex2f(x + size, y)
                glVertex2f(x + size, y + size)

    glEnd()

def draw_text(x, y, text, color=(1, 1, 1)):
    glColor3f(*color)
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def draw_rect(x, y, w, h, color=(1, 1, 1), filled=True):
    glColor3f(*color)
    if filled:
        glBegin(GL_QUADS)
    else:
        glLineWidth(1.0)
        glBegin(GL_LINE_LOOP)
    glVertex2f(x, y)
    glVertex2f(x + w, y)
    glVertex2f(x + w, y + h)
    glVertex2f(x, y + h)
    glEnd()

def draw_ui(ui_state):
    # Panel background
    draw_rect(-1.0, -1.0, 0.6, 2.0, (0.05, 0.05, 0.1))
    
    # Title
    draw_text(-0.9, 0.8, "OLIT'S MAZE", (0.0, 0.7, 1.0))
    
    # Rows input
    draw_text(-0.9, 0.6, "Rows:")
    row_color = (0.2, 0.2, 0.4) if ui_state['focus'] == 'rows' else (0.1, 0.1, 0.2)
    draw_rect(-0.9, 0.52, 0.4, 0.08, row_color)
    draw_text(-0.85, 0.54, ui_state['rows_text'])
    
    # Cols input
    draw_text(-0.9, 0.4, "Cols:")
    col_color = (0.2, 0.2, 0.4) if ui_state['focus'] == 'cols' else (0.1, 0.1, 0.2)
    draw_rect(-0.9, 0.32, 0.4, 0.08, col_color)
    draw_text(-0.85, 0.34, ui_state['cols_text'])
    
    # Generate Button (Deep Blue)
    gen_color = (0.0, 0.3, 0.6)
    draw_rect(-0.9, 0.1, 0.4, 0.12, gen_color)
    draw_text(-0.82, 0.14, "GENERATE")
    
    solve_color = (0.0, 0.5, 0.9) if ui_state['state'] == 'READY_TO_SOLVE' else (0.1, 0.2, 0.3)
    draw_rect(-0.9, -0.1, 0.4, 0.12, solve_color)
    draw_text(-0.78, -0.06, "SOLVE")

    # Algorithm Selection
    draw_text(-0.9, -0.18, "Algorithm:", (0.7, 0.7, 0.7))
    
    dfs_color = (0.0, 0.6, 0.3) if ui_state['algo'] == 'DFS' else (0.1, 0.2, 0.1)
    draw_rect(-0.9, -0.3, 0.18, 0.08, dfs_color)
    draw_text(-0.85, -0.28, "DFS")

    bfs_color = (0.0, 0.6, 0.3) if ui_state['algo'] == 'BFS' else (0.1, 0.2, 0.1)
    draw_rect(-0.68, -0.3, 0.18, 0.08, bfs_color)
    draw_text(-0.63, -0.28, "BFS")
    
    status_map = {
        'IDLE': 'Ready to start',
        'GENERATING': 'Building maze...',
        'READY_TO_SOLVE': 'Generated!',
        'SOLVING': 'Searching...',
        'FINISHED': 'Solved!'
    }
    draw_text(-0.9, -0.4, "Status:", (0.7, 0.7, 0.7))
    draw_text(-0.9, -0.48, status_map.get(ui_state['state'], ui_state['state']), (1, 1, 1))

def box(r, c, s, ox, oy):
    x = ox + (c - 1) * s
    y = oy + (r - 1) * s
    glBegin(GL_QUADS)
    glVertex2f(x + 0.1*s, y + 0.1*s)
    glVertex2f(x + 0.9*s, y + 0.1*s)
    glVertex2f(x + 0.9*s, y + 0.9*s)
    glVertex2f(x + 0.1*s, y + 0.9*s)
    glEnd()