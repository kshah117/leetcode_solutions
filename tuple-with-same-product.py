class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        same = 0
        products = {}
        N = len(nums)
        for a in range(N):
            for b in range(a + 1, N):
                products[nums[a] * nums[b]] = products.get(nums[a] * nums[b], 0) + 1

        for k, v in products.items():
            if v > 1:
                same += 8 * (v * (v - 1)) // 2

        return same
