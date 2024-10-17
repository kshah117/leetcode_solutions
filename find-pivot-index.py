class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum = sum(nums) - 0
        lsum = 0
        for i in range(len(nums)):
            if lsum == rsum - lsum - nums[i]:
                return i
            lsum += nums[i]

        return -1