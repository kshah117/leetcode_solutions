from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == "+":
                s.append(s.pop() + s.pop())
            elif t == "-":
                n2 = s.pop()
                n1 = s.pop()
                s.append(n1 - n2)
            elif t == "*":
                s.append(s.pop() * s.pop())
            elif t == "/":
                n2 = s.pop()
                n1 = s.pop()
                s.append(int(n1 / n2))
            else:
                s.append(int(t))

        return s.pop()
