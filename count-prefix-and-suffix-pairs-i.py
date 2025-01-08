class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            l = len(str1)
            if str1 == str2[:l] and str1 == str2[-(l):]:
                return True

        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count
