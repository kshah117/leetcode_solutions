class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)

        right = -1
        same = 0
        freq = {}
        total = 0
        for left in range(N):
            while same < k and right + 1 < N:
                right += 1
                same += freq.get(nums[right], 0)
                freq[nums[right]] = freq.get(nums[right], 0) + 1

            if same >= k:
                total += N - right

            freq[nums[left]] -= 1
            same -= freq[nums[left]]
        return total
