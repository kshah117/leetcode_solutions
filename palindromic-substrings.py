class Solution:
    def countSubstrings(self, s: str) -> int:
        subs = []
        N = len(s)
        
        def expand(x, y):
            while x >= 0 and y < N and s[x] == s[y]:
                subs.append(s[x:y + 1])
                x -= 1
                y += 1
        
        for i in range(N):
            expand(i, i)
            expand(i, i + 1)
        return len(subs)


