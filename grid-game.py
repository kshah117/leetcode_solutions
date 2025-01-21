class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        row_one_sum = sum(grid[0])
        row_two_sum = 0
        min_score = float("inf")

        for i in range(COLS):
            row_one_sum -= grid[0][i]
            min_score = min(min_score, max(row_one_sum, row_two_sum))
            row_two_sum += grid[1][i]

        return min_score