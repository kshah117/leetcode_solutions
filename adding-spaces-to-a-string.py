class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ret = []
        space_index = 0
        for i in range(len(s)):
            if space_index < len(spaces) and i == spaces[space_index]:
                ret.append(" ")
                space_index += 1

            ret.append(s[i])

        return ''.join(ret)