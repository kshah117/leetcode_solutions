class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        visited = {}
        ROWS = len(grid)
        COLS = len(grid[0])
        com = 0

        for r in range(ROWS):
            if not grid[r].count(1) > 1:
                continue
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue
                else:
                    com += 1
                    visited[(r, c)] = True

        for c in range(COLS):
            temp_col = [grid[r][c] for r in range(ROWS)]
            if not temp_col.count(1) > 1:
                continue
            for r in range(ROWS):
                if grid[r][c] == 0:
                    continue
                else:
                    if not visited.get((r, c)):
                        com += 1
                        visited[(r, c)] = True
        return com
