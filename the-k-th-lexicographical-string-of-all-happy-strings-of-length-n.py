class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy = {"a": n, "b": n, "c": n}
        ret = []

        def helper(s):
            if len(s) > n:
                return
            if len(s) == n:
                ret.append("".join(s))

            for k, v in happy.items():
                if v == 0:
                    continue
                if len(s) > 0 and s[-1] == k:
                    continue

                happy[k] = v - 1
                s.append(k)
                helper(s)
                s.pop(-1)
                happy[k] = v + 1

        helper([])
        return ret[k - 1] if k <= len(ret) else ""
