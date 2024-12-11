class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        minutes = -1
        fresh = 0
        queue = []

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        queue.append((-1, -1))

        while queue:
            r, c = queue.pop(0)
            if r == -1:
                minutes += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for d in directions:
                    neighbor_row, neighbor_column = r + d[0], c + d[1]
                    if 0 <= neighbor_row < ROWS and 0 <= neighbor_column < COLUMNS:
                        if grid[neighbor_row][neighbor_column] == 1:
                            grid[neighbor_row][neighbor_column] = 2
                            queue.append((neighbor_row, neighbor_column))
                            fresh -= 1

        return minutes if fresh == 0 else -1
