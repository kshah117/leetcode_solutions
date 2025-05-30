class Solution:
    def checkValidString(self, s: str) -> bool:
        special = []
        stack = []

        for i, c in enumerate(s):
            if c == "(":
                stack.insert(0, i)
            elif c == ")":
                if stack:
                    stack.pop(0)
                elif special:
                    special.pop(0)
                else:
                    return False
            else:
                special.insert(0, i)

        while stack and special:
            if stack[0] < special[0]:
                stack.pop(0)
                special.pop(0)
            else:
                return False

        return not stack
