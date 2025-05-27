class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        l1 = 0
        l2 = 0

        for i in range(1, n + 1):
            l1 += i if i % m != 0 else 0
            l2 += i if i % m == 0 else 0
        return l1 - l2