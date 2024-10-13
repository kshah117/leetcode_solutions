class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr_sum = n + nums[l] + nums[r]
                if curr_sum == 0:
                    ret.append([n, nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
        return ret
