class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        odd_count = 0
        for f in freq:
            if f % 2 == 1:
                odd_count += 1

        if odd_count > k:
            return False
        else:
            return True

