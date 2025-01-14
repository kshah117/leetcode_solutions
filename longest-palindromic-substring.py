class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        if N < 2:
            return s

        def expand(l, r):
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        pos = [0, 0]
        for i in range(N):
            odd_len = expand(i, i)

            if odd_len > pos[1] - pos[0] + 1:
                dist = odd_len // 2
                pos = [i - dist, i + dist]

            even_len = expand(i, i + 1)
            if even_len >  pos[1] - pos[0] + 1:
                dist = (even_len // 2) - 1
                pos = [i - dist, i + 1+ dist]

        return s[pos[0] : pos[1] + 1]
