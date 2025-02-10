class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        N = len(intervals)
        merged = []
        for i in range(N):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]

            if not merged or merged[-1][1] < cur_start:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(cur_end, merged[-1][1])

        return merged

            
