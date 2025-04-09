class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        for n in nums:
            if n < k:
                return -1
            freq[n] = freq.get(n, 0) + 1
        num_ops = 0
        for key in freq:
            if key > k:
                num_ops += 1
        return num_ops