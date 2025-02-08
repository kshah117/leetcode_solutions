class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        int_start = newInterval[0]
        int_end = newInterval[1]
        new = []
        N = len(intervals)
        added = False

        if int_end < intervals[0][0]:
            new.append(newInterval)
            added = True

        for i in range(N):
            cur = intervals[i]
            cur_start = cur[0]
            cur_end = cur[1]

            if cur_end < int_start or cur_start > int_end:
                new.append(cur)

                if (
                    int_start > cur_end
                    and i < (N - 1)
                    and int_end < intervals[i + 1][0]
                ):
                    new.append(newInterval)
                    added = True
            else:
                if added:
                    continue
                temp_add = []
                temp_add.append(min(cur_start, int_start))
                for x in range(i, N):
                    if intervals[x][0] > int_end:
                        temp_add.append(max(intervals[x - 1][1], int_end))
                        break
                    elif intervals[x][1] > int_end:
                        temp_add.append(intervals[x][1])
                        break
                    else:
                        continue

                if len(temp_add) < 2:
                    temp_add.append(max(cur_end, int_end))

                if not added:
                    new.append(temp_add)
                    added = True

        if not added:
            new.append(newInterval)
            added = True

        return new
