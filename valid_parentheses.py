class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        closing_brackets = ("]", ")", "}")
        opening_brackets_dict = {"]": "[", ")": "(", "}": "{"}

        for b in s:
            if b in closing_brackets:
                if not l or l[-1] != opening_brackets_dict[b]:
                    return False
                else:
                    l.pop(-1)
            else:
                l.append(b)

        if len(l) > 0:
            return False

        return True


tc = "()[]{}"
sol = Solution()
print(sol.isValid(tc))
