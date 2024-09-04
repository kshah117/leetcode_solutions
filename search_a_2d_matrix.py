from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0]) - 1

        for row in matrix:
            if row[0] <= target and target <= row[r]:
                while l <= r:
                    mid = int((l + r) / 2)

                    if row[mid] == target:
                        return True
                    elif row[mid] >= target:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False

        return False
    