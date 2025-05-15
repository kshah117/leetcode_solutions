class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        N = len(words)
        ret = [words[0]]
        for i in range(1, N):
            if groups[i] != groups[i - 1]:
                ret.append(words[i])
        return ret
