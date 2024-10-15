class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = {}

        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[nums[i]] = i
                continue
            
            if abs(temp[nums[i]] - i) <= k:
                return True
            else:
                temp[nums[i]] = i
        return False