class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            arr[i] = min(arr[i - 1] + cost[i - 1], arr[i - 2] + cost[i - 2])

        return arr[-1]
