class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        sub = []
        cache = {}
        
        if sum(candidates) < target:
            return []

        candidates.sort()

        def helper(i):
            if sum(sub) == target:
                if tuple(sub) not in cache:
                    ret.append(sub.copy())
                    cache[tuple(sub)] = True
            
            if i == len(candidates) or sum(sub) > target:
                return

            sub.append(candidates[i])
            helper(i + 1)
            sub.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            helper(i + 1)

        helper(0)
        return ret