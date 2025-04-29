class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        N = len(nums)
        l = 0
        count = 0
        cur_count = 0
        for r in range(N):
            if nums[r] == target:
                cur_count += 1

            while cur_count == k:
                if nums[l] == target:
                    cur_count -= 1
                l += 1

            count += l

        return count
