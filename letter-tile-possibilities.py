class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        f = {}

        def backtracking():
            total = 0
            for k, v in f.items():
                if f[k] == 0:
                    continue
                
                total += 1
                f[k] -= 1
                total += backtracking()
                f[k] += 1
            return total


        for c in tiles:
            f[c] = f.get(c, 0) + 1
        
        return backtracking()
