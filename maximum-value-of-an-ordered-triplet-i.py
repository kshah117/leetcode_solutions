class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ret = 0
        for x in range(1, len(nums) - 1):
            i = max(nums[0:x])
            j = nums[x]
            k = max(nums[x + 1:])
            val =(i - j) * k
            ret = max(ret, val)

        return ret
