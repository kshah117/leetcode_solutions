class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            t1 = 0
            t2 = 0

            for c in nums:
                temp = t1
                t1 = max(c + t2, t1)
                t2 = temp

            return t1

        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:]))
