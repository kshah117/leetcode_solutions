class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ret = []
        sub = []

        def helper(i):
            if i == len(digits):
                if sub:
                    ret.append(("").join(sub))
                return 

            letters = m[digits[i]]
            for c in letters:
                sub.append(c)
                helper(i + 1)
                sub.pop()
        
        helper(0)
        return ret

