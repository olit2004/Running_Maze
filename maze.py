
# the maze data structure
class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.up = [[1 for _ in range(cols + 1)] for _ in range(rows + 1)]
        self.right = [[1 for _ in range(cols + 1)] for _ in range(rows + 1)]
        self.seen = [[False for _ in range(cols + 1)] for _ in range(rows + 1)]
        self.curr = None
        self.stack = []
        self.built = False
        self.trace = []
        self.route = []
        self.dead = set()
        self.visited = set()
        self.queue = []
        self.parents = {}
        self.solved = False
        self.start = None
        self.end = None