class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        recent_interval_end = -inf
        removed = 0

        for intercal_start, interval_end in intervals:
            if intercal_start >= recent_interval_end:
                recent_interval_end = interval_end
            else:
                removed += 1

        return removed
