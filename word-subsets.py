from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        ret = []
        counts_b = {}

        for w2 in words2:
            w2_counts = Counter(w2)
            for ch in w2_counts:
                counts_b[ch] = max(w2_counts[ch], counts_b.get(ch, 0))

        for a in words1:
            to_add = True
            for ch in counts_b:
                if a.count(ch) < counts_b[ch]:
                    to_add = False
                    break
            if to_add:
                ret.append(a)
        return ret
