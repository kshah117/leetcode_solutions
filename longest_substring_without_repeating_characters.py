class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        ret = 0
        for c in s:
            if c in temp:
                ti = temp.index(c)
                ret = max(ret, len(temp))
                temp.append(c)
                temp = temp[ti + 1:]
            else:
                temp.append(c)
        ret = max(ret, len(temp))
        return ret

sol = Solution()
s = "aabaab!bb"
print(sol.lengthOfLongestSubstring(s))