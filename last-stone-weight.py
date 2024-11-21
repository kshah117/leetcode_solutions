class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            y = stones.pop(-1)
            x = stones.pop(-1)
            res = y - x
            if res > 0:
                stones.append(res)
                stones.sort()
        
        if stones:
            return stones[0]
        else:
            return 0
