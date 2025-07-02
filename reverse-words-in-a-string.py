class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        l = 0
        r = len(words) - 1

        while l < r:
            if not words[l]:
                l += 1
                continue
            if not words[r]:
                r -= 1
                continue
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1

        revered_words = " ".join([w for w in words if w])
        revered_words = revered_words.strip()
        return revered_words