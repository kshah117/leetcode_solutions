class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COL = len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        pacific = []
        atlantic = []

        for i in range(ROWS):
            pacific.append((i, 0))
            atlantic.append((i, COL - 1))

        for i in range(COL):
            pacific.append((0, i))
            atlantic.append((ROWS - 1, i))

        def bfs(queue):
            reach = set()
            while queue:
                r, c = queue.pop(0)
                reach.add((r, c))
                for d1, d2 in directions:
                    neighbor_row = r + d1
                    neighbor_col = c + d2
                    if (
                        0 > neighbor_col
                        or neighbor_col >= COL
                        or 0 > neighbor_row
                        or neighbor_row >= ROWS
                    ):
                        continue

                    if (neighbor_row, neighbor_col) in reach:
                        continue

                    if heights[neighbor_row][neighbor_col] < heights[r][c]:
                        continue

                    queue.append((neighbor_row, neighbor_col))

            return reach

        pacific_reach = bfs(pacific)
        atlantic_reach = bfs(atlantic)

        return list(pacific_reach.intersection(atlantic_reach))
