class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while len(s) > 1:
            if i == len(s) - 1:
                return s
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                s = s[:i] + s[i + 2 :]
                i = 0
                continue
            i += 1
        return s


sol = Solution()
print(sol.makeGood("abBAcC"))
