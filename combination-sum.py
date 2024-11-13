class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        sub = []
        l = len(candidates)

        def dfs(i, x):
            if x > target or i >= l:
                return
            if x == target:
                ret.append(sub.copy())
                return

            sub.append(candidates[i])
            dfs(i, sum(sub))

            sub.pop()
            dfs(i + 1, sum(sub))

        dfs(0, 0)
        return ret
