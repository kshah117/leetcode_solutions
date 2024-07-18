from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        def helper(openN, closeN):
            if len(s) == n * 2:
                res.append("".join(s))

            if openN < n:
                s.append("(")
                helper(openN + 1, closeN)
                s.pop()
            if closeN < openN:
                s.append(")")
                helper(openN, closeN + 1)
                s.pop()

        helper(0, 0)
        return res
