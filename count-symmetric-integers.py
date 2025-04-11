class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric = 0
        for n in range(low, high + 1):

            num_str = str(n)
            if len(num_str) % 2 == 1:
                continue
            m = len(num_str) // 2

            pref = sum([int(c) for c in num_str[: m]])
            suf = sum([int(c) for c in num_str[m:]])

            if pref == suf:
                symmetric += 1

        return symmetric
