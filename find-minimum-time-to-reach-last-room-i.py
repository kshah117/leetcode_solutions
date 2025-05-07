class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ROWS = len(moveTime)
        COLUMNS = len(moveTime[0])
        cache = [[inf] * COLUMNS for _ in range(ROWS)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        heap = []
        heappush(heap, (0, 0, 0))

        while heap:
            time, r, c = heappop(heap)
            if r == ROWS - 1 and c == COLUMNS - 1:
                continue

            for d in directions:
                new_row = r + d[0]
                new_column = c + d[1]
                if (
                    new_row == ROWS
                    or new_column == COLUMNS
                    or new_row == -1
                    or new_column == -1
                ):
                    continue
                new_time = max(moveTime[new_row][new_column], time) + 1
                if new_time < cache[new_row][new_column]:
                    cache[new_row][new_column] = new_time
                    heappush(heap, (new_time, new_row, new_column))

        return cache[-1][-1]
