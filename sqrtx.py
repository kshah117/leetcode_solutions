class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        # for i in range(x + 1):
        #     if i * i == x:
        #         return i
        #     elif i * i > x:
        #         return i - 1


        l = 0
        r = x

        while l < r - 1:
            m = (l + r) // 2

            if m * m == x:
                return m
            elif m * m > x:
                r = m
            else:
                l = m

        return l