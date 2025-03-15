class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l = 1
        r = max(nums)
        N = len(nums)

        while l < r:
            m = (l + r) // 2

            temp_k = 0
            i = 0

            while i < N:
                if nums[i] <= m:
                    temp_k += 1
                    i += 2
                else:
                    i += 1
            
            if temp_k >= k:
                r = m
            else:
                l = m + 1

        return l