class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        val = 0
        for d in derived:
            val = xor(d, val)

        return val == 0