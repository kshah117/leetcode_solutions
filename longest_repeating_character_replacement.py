class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        m = {}
        ret = 0
        freq_c = 0

        for r in range(len(s)):
            m[s[r]] = m.get(s[r], 0) + 1
            freq_c = max(freq_c, m[s[r]])
            while (r - l + 1) - freq_c > k:
                m[s[l]] -= 1
                l += 1
                
            ret = max(ret, r - l + 1)

        return ret
            

                