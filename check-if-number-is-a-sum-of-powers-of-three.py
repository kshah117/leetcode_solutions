class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def helper(cur, x):
            num = cur + 3**x
            if num == n:
                return True
            if num > n:
                return False

            return helper(num, x + 1) or helper(cur, x + 1)

        return helper(0, 0)
