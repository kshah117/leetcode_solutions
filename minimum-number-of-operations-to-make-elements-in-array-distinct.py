class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            if freq.get(n):
                return (i + 1) // 3 if (i + 1) % 3 == 0 else ((i + 1) // 3) + 1
            freq[n] = freq.get(n, 0) + 1

        return 0
