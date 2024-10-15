from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = len(prices)
        min_price = prices[0]
        max_profit = 0
        for i in range(d):
            curr_price = prices[i]
            min_price = min(min_price, curr_price)
            max_profit = max(max_profit, curr_price - min_price)
        return max_profit