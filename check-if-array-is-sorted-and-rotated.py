class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        decreasing = 0
        for i in range(1, N):
            prev = nums[i - 1]
            cur = nums[i]

            if cur < prev:
                decreasing += 1

            if decreasing > 1:
                return False

        if decreasing == 1:
            if nums[N - 1] > nums[0]:
                return False

        return True
