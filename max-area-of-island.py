class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        covered = {}
        max_area = 0

        def dfs(r, c):
            if (
                (r, c) in covered
                or r < 0
                or c < 0
                or r == len(grid)
                or c == len(grid[0])
                or grid[r][c] == 0
            ):
                return 0

            covered[(r, c)] = True

            down = dfs(r + 1, c)
            up = dfs(r - 1, c)
            right = dfs(r, c + 1)
            left = dfs(r, c - 1)

            return 1 + left + down + up + right

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in covered:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area
