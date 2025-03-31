class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        vals = list(freq.values())
        vals.sort(reverse=True)
        length = 0
        for f in vals:
            if f % 2 == 1:
                length += f if length % 2 == 0 else f - 1
            else:
                length += f

        return length