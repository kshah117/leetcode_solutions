class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        rob_next = nums[N - 1]
        rob_next_plus_one = 0

        for i in range(N - 2, -1, -1):
            cur = max(rob_next, rob_next_plus_one + nums[i])

            rob_next_plus_one = rob_next
            rob_next = cur

        return rob_next
