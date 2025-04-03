class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)

        max_k = [0] * n
        max_k[-1] = nums[-1]

        for k_index in range(n - 2, 1, -1):
            max_k[k_index] = max(nums[k_index], max_k[k_index + 1])

        i = nums[0]
        for x in range(1, len(nums) - 1):
            j = nums[x]
            i = max(i, nums[x - 1])
            k = max_k[x + 1]
            ret = max(ret, (i - j) * k)

        return ret
