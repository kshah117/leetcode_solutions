class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        res = []
        nums.sort()

        for a in range(N):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, N):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                c = b + 1
                d = N - 1
                while c < d:
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        c += 1
                        d -= 1

                    elif nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1
                    else:
                        c += 1
        return res
