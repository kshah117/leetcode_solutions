class Solution:
    def minimumLength(self, s: str) -> int:
        m = dict(Counter(s))
        l = 0

        for k, v in m.items():
            if v % 2 == 1:
                l += 1
            else:
                l += 2
        return l
