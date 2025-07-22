class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        max_sum = 0
        cur_sum = 0
        l = 0
        seen = set()

        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                cur_sum -= nums[l]
                l += 1

            seen.add(nums[r])
            cur_sum += nums[r]
            max_sum = max(cur_sum, max_sum)

        return max_sum
