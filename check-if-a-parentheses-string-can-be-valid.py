class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        open_count = 0
        unlocks = 0

        for i in range(len(s)):
            if s[i] == "(" or locked[i] == "0":
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    return False

        unlocks = 0
        close_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ")" or locked[i] == "0":
                close_count += 1
            else:
                if close_count > 0:
                    close_count -= 1
                else:
                    return False

        return True
