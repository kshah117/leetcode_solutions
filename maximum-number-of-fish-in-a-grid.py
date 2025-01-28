class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_fish = 0

        def dfs(r, c, fishes):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 0
            
            fishes = grid[r][c]
            grid[r][c] = 0

            for d in directions:
                nr, nc = r + d[0], c + d[1]
                fishes += dfs(nr, nc, fishes)
            return fishes

        for i in range(R):
            for j in range(C):
                if grid[i][j] > 0:
                    fishes = dfs(i, j, 0)
                    max_fish = max(max_fish, fishes)

        return max_fish