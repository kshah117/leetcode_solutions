class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS = len(isWater)
        COLS = len(isWater[0])

        heights = [[-1] * COLS for _ in range(ROWS)]


        for i in range(ROWS):
            for j in range(COLS):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    heights[i][j] = 0

        while queue:
            r, c = queue.pop(0)
            for d in directions:
                nr, nc = r + d[0], c + d[1]

                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] == -1:
                    heights[nr][nc] = heights[r][c] + 1
                    queue.append((nr, nc))

        return heights
