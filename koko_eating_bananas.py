import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r

        while l <= r:
            m = int((l + r)/2)
            temp_h = 0
            for i in piles:
                temp_h += math.ceil(i/m)
            
            if temp_h > h:
                l = m + 1
            else:
                k = min(m, k)
                r = m - 1
                
        return k
    
sol = Solution()
piles = [3,6,7,11]
h = 8
print(sol.minEatingSpeed(piles, h))