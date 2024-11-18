class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ret = []
        subset = []
        cache = {}

        def helper(i):
            if i == len(nums):
                if tuple(subset) not in cache:
                    self.ret.append(subset.copy())
                    cache[tuple(subset)] = True
                return

            subset.append(nums[i])
            helper(i + 1)
            subset.pop()
            helper(i + 1)

        helper(0)
        return self.ret