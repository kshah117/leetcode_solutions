class Solution:
    def robotWithString(self, s: str) -> str:
        freq = Counter(s)

        t = []
        paper = []

        for x in s:
            t.append(x)

            freq[x] -= 1
            if freq[x] == 0:
                freq.pop(x)

            min_char = min(freq.keys()) if freq else "a"

            while t and t[-1] <= min_char:
                paper += t.pop()

        return "".join(paper + t[::-1])
