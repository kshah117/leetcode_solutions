
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for c in tasks:
            freq[ord(c) - ord("A")] += 1

        time = 0

        pq = [-f for f in freq if f > 0]
        heapq.heapify(pq)

        while pq:
            cycle = n + 1
            next_itteration = []
            task_count = 0

            while cycle > 0 and pq:
                cur = -heappop(pq)
                if cur > 1:
                    next_itteration.append(cur - 1)
                task_count += 1
                cycle -= 1
            
            for x in next_itteration:
                heappush(pq, -x)

            time += task_count if not pq else n + 1
        return time
            

