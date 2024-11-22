import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            dist = (p[0]**2 + p[1]**2)**0.5
            if len(heap) < k:
                heapq.heappush(heap,(-dist, p))
            else:
                heapq.heappushpop(heap,(-dist, p))

        ret = []
        for dist, p in heap:
            ret.append(p)
        return ret

        

            