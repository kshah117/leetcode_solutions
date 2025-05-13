class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7

        counter = [0] * 26

        for ch in s:
            counter[ord(ch) - ord('a')] += 1

        for _ in range(t):
            next_round = [0] * 26
            next_round[0] = counter[25]
            next_round[1] = (counter[25] + counter[0]) % MOD

            for i in range(2, 26):
                next_round[i] = counter[i - 1]
            counter = next_round

        return sum(counter) % MOD
