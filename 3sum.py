class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ret = []
        for x in range(N):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            i = nums[x]
            l = x + 1
            r = N - 1
            while l < r:
                j = nums[l]
                k = nums[r]
                if i + j + k == 0:
                    ret.append([i, j, k])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1
                elif i + j + k > 0:
                    r -= 1
                else:
                    l += 1

        return ret
