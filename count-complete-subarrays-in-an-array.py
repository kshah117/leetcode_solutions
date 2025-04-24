class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique = len(set(nums))
        complete = 0
        N = len(nums)

        for i in range(N):
            sub_array = set()
            for j in range(i, N):
                sub_array.add(nums[j])
                if len(sub_array) == unique:
                    complete += N - j
                    break

        return complete
