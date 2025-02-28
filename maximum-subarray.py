class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        ret = temp_sub = nums[0]
        for i in range(1, N):
            if temp_sub < 0 and nums[i] > temp_sub:
                temp_sub = nums[i]
            else:
                temp_sub += nums[i]

            ret = max(ret, temp_sub)
        return ret
