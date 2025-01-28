class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        max_till_cur = nums[0]
        min_till_now = nums[0]
        max_product = nums[0]

        for i in range(1, N):
            n = nums[i]
            temp_max = max(n, max_till_cur * n, min_till_now * n)
            min_till_now = min(n, max_till_cur * n, min_till_now * n)

            max_till_cur = temp_max
            max_product = max(max_till_cur, max_product)

        return max_product