class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left_product = [1] * N
        right_product = [1] * N

        for i in range(1, N):
            left_product[i] = (left_product[i - 1] * nums[i - 1])


        for i in range(1, N):
            right_product[-(i + 1)] = right_product[-i] * nums[-i]


        final = [1] * N
        for i in range(N):
            final[i] = left_product[i] * right_product[i]
        return final
