class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total_candies = sum(candies)
        if k > total_candies:
            return 0
        l = 1
        r = max(candies)

        while l <= r:
            m = (l + r) // 2

            piles = sum(cur_pile // m for cur_pile in candies)

            if piles < k:
                r = m - 1
            else:
                l = m + 1

        return r
