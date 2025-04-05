class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0

        def helper(i, temp_xor):
            if i == len(nums):
                self.total += temp_xor
                return

            new_temp_xor = temp_xor ^ nums[i]
            helper(i + 1, new_temp_xor)
            helper(i + 1, temp_xor)

        helper(0, 0)
        return self.total
