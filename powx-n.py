class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binary_exponentiation(x, n):
            if n == 0:
                return 1.0
            elif n < 0:
                return 1 / binary_exponentiation(x, -n)
            else:
                if n % 2 == 0:
                    return binary_exponentiation(x * x, n // 2)
                else:
                    return x * binary_exponentiation(x * x, (n - 1) // 2)

        return binary_exponentiation(x, n)
