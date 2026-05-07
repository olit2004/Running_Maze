class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.northWall = [
            [1 for _ in range(cols)]
            for _ in range(rows + 1)
        ]

        self.eastWall = [
            [1 for _ in range(cols + 1)]
            for _ in range(rows)
        ]

        # Track visited cells
        self.visited = [
            [False for _ in range(cols)]
            for _ in range(rows)
        ]