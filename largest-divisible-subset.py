class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        dp = [1] * N
        prev = [-1] * N

        max_len = 0
        max_subset_index = 0

        nums.sort()
        for i in range(N):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

                if dp[i] > max_len:
                    max_len = dp[i]
                    max_subset_index = i

        ret = []
        while max_subset_index != -1:
             ret.append(nums[max_subset_index])
             max_subset_index = prev[max_subset_index]
        return ret
