from OpenGL.GL import *

def draw(maze, size):
    ox = -0.9
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

def box(r, c, s, ox, oy):
    x = ox + (c - 1) * s
    y = oy + (r - 1) * s
    glBegin(GL_QUADS)
    glVertex2f(x + 0.1*s, y + 0.1*s)
    glVertex2f(x + 0.9*s, y + 0.1*s)
    glVertex2f(x + 0.9*s, y + 0.9*s)
    glVertex2f(x + 0.1*s, y + 0.9*s)
    glEnd()