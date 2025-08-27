class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            while i < len(nums) and nums[i] == nums[i - 1]:
                nums.pop(i)
                continue
            i += 1
        return len(nums)
            