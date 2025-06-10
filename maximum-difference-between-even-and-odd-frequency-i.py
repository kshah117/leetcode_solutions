class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_freq = [i for i in freq.values() if i % 2 == 1]
        even_freq = [i for i in freq.values() if i % 2 == 0]
        return max(odd_freq) - min(even_freq) 
