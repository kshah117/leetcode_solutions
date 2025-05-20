class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1

        operations = []
        cur_operations = 0
        for cur_diff in diff:
            cur_operations += cur_diff
            operations.append(cur_operations)

        for i in range(n):
            if nums[i] > operations[i]:
                return False
        return True
