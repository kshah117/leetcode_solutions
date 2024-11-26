class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hs = -1
        ht = -1
        scores = {}
        for i in range(n):
            count = 0
            for j in range(n):
                count += grid[i][j]
            scores[i] = count

        for k, v in scores.items():
            if v > hs:
                ht = k
                hs = v

        return ht
