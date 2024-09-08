from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        lowest = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                lowest = min(lowest, nums[l])
                break
            
            m = (l + r) // 2
            mid_element = nums[m]
            lowest = min(lowest, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return lowest
    
sol = Solution()
nums = [4,5,6,7,0,1,2]
print(sol.findMin(nums))