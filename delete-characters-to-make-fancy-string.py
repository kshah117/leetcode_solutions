class Solution:
    def makeFancyString(self, s: str) -> str:
        N = len(s)
        if N < 2:
            return s

        new_s = [s[0], s[1]]

        for i in range(2, N):
            if s[i] == new_s[-1] and s[i] == new_s[-2]:
                continue
            new_s.append(s[i])

        return "".join(new_s)
