class Maze:

    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols

        # Horizontal walls
        # northWall[r][c]
        #
        # rows + 1 because:
        # extra row represents bottom boundary
        self.northWall = [
            [1 for _ in range(cols)]
            for _ in range(rows + 1)
        ]

        # Vertical walls
        # eastWall[r][c]
        #
        # cols + 1 because:
        # extra column represents right boundary
        self.eastWall = [
            [1 for _ in range(cols + 1)]
            for _ in range(rows)
        ]

        # Tracks visited cells during maze generation
        self.visited = [
            [False for _ in range(cols)]
            for _ in range(rows)
        ]

        # Cells currently in solver path
        self.solution_path = []

        # Dead-end cells found during solving
        self.dead_ends = set()