class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        sub_sums = {0}

        for i in range(len(nums) - 1, -1, -1):
            new_sub_sums = set()
            for t in sub_sums:
                if (t + nums[i]) == target:
                    return True
                new_sub_sums.add(t + nums[i])
                new_sub_sums.add(t)
            sub_sums = new_sub_sums

        return False
