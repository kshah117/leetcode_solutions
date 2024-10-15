from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        index = -1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            
            if nums[l] <=  nums[m]:
                if nums[l] > target or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
        return index


sol = Solution()
nums = [5,1,2,3,4]
target = 1
print(sol.search(nums, target))