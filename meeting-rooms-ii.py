class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []
        heappush(heap, intervals[0][1])

        for i in range(1, len(intervals)):
            prev = heap[0]
            cur = intervals[i]
            if cur[0] < prev:
                heappush(heap, cur[1])
            else:
                heappushpop(heap, cur[1])

      
        return len(heap)