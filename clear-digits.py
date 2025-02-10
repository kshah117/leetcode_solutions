class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for ch in s:
            if ord(ch) >= ord('0') and ord(ch) <= ord('9'):
                stack.pop(-1)
                continue
            stack.append(ch)

        ret = "".join(stack)
        return ret
