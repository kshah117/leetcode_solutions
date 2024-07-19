from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ret = [0] * len(temperatures)
        for n, t in enumerate(temperatures):
            while s and s[-1][1] < t:
                prev_n = s.pop()[0]
                ret[prev_n] = n - prev_n
            s.append((n, t))
        return ret
