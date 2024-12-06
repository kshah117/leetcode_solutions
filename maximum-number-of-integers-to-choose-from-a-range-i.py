class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        banned = list(set(banned))
        max_count = 0
        cur_sum = 0

        for i in range(1, n + 1):
            if max_count == n or i > maxSum:
                break
            if cur_sum + i <= maxSum:
                if i not in banned:
                    max_count += 1
                    cur_sum += i
            else:
                break

        return max_count
