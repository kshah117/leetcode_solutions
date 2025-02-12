class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sums = {}
        ret = -1
        for n in nums:
            x = n
            temp_sum = 0
            while x:
                temp_sum += x % 10
                x = x // 10
            if digit_sums.get(temp_sum):
                digit_sums[temp_sum].append(n)
            else:
                digit_sums[temp_sum] = [n]

        for k, v in digit_sums.items():
            if len(v) < 2:
                continue

            v.sort()
            ret = max(ret, v[-1] + v[-2])

        return ret
