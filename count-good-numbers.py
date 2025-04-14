class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9) + 7

        def calculate(x, n):
            ret = 1
            while n > 0:
                if n % 2 == 1:
                    ret *= x % mod
                x = (x * x) % mod
                n = n // 2
            return ret

        return calculate(5, (n + 1) // 2) * calculate(4, n //  v2) % mod
