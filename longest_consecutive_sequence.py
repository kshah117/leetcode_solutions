from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        start = 0
        end = 0
        max_len = 0

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                end += 1
            else:
                max_len = max(max_len, end - start + 1)
                start = i
                end = i
        return max(max_len, end - start + 1)


sol = Solution()
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums=nums))