class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count_subarrays_map = {0: 1}
        N = len(nums)
        result = 0
        prefix = 0

        for i in range(N):
            if nums[i] % modulo == k:
                prefix += 1

            result += count_subarrays_map.get((prefix - k + modulo) % modulo, 0)
            count_subarrays_map[prefix % modulo] = (
                count_subarrays_map.get(prefix % modulo, 0) + 1
            )
        
        return result
