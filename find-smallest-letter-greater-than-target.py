class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1

        while l <= r:
            m = l + (r - l) // 2

            if ord(letters[m]) <= ord(target):
                l = m + 1
            else:
                r = m - 1

        if l > len(letters) - 1:
            return letters[0]
        return letters[l]
