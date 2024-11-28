class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        covered = {}
        self.islands = 0

        def helper(r, c):
            if (r, c) in covered:
                return 0
            if (
                r < 0
                or c < 0
                or r >= len(grid)
                or c >= len(grid[0])
                or grid[r][c] == "0"
            ):
                return 0

            covered[(r, c)] = True

            helper(r + 1, c)
            helper(r - 1, c)
            helper(r, c + 1)
            helper(r, c - 1)

            return 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in covered:
                    self.islands += helper(i, j)

        return self.islands
