class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 0
        dec = 0
        N = len(nums)

        temp_i = 0
        temp_d = 0
        for i in range(1, N):
            prev = nums[i - 1]
            cur = nums[i]

            if prev < cur:
                temp_i += 1
                dec = max(dec, temp_d)
                temp_d = 0
            elif prev > cur:
                temp_d += 1
                inc = max(inc, temp_i)
                temp_i = 0
            else:
                inc = max(inc, temp_i)
                temp_i = 0
                dec = max(dec, temp_d)
                temp_d = 0
                continue

        dec = max(dec, temp_d)
        inc = max(inc, temp_i)
        return max(1, max(inc, dec) + 1)