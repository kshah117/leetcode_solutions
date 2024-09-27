from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = {}

        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[nums[i]] = [i]
                continue
            
            if abs(temp[nums[i]][-1] - i) <= k:
                return True
            else:
                temp[nums[i]].append(i)
            
        return False
    
sol = Solution()
nums = [1,0,1,1]
k = 1
print(sol.containsNearbyDuplicate(nums, k))