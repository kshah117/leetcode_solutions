class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        return self.count_powerful(str(finish), s, limit) - self.count_powerful(
            str(start - 1), s, limit
        )

    def count_powerful(self, x, s, limit):
        if len(x) < len(s):
            return 0
        if len(x) == len(s):
            return 1 if x >= s else 0

        suffix = x[len(x) - len(s) :]
        counter = 0
        prefix_len = len(x) - len(s)

        for i in range(prefix_len):
            if limit < int(x[i]):
                counter += (limit + 1) ** (prefix_len - i)
                return counter
            counter += int(x[i]) * (limit + 1) ** (prefix_len - 1 - i)

        if suffix >= s:
            counter += 1

        return counter
