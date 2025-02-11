class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        x = s.split(part, 1)
        new_w = "".join(x)

        while part in new_w:
            x = new_w.split(part, 1)
            new_w = "".join(x)

        return new_w
