class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        N = len(tops)
        freq = {}
        min_operations = N
        for i in range(N):
            top_i = tops[i]
            bottom_i = bottoms[i]

            if top_i == bottom_i:
                freq[top_i] = freq.get(top_i, 0) + 1
            else:
                freq[top_i] = freq.get(top_i, 0) + 1
                freq[bottom_i] = freq.get(bottom_i, 0) + 1

        possible = []
        for num, f in freq.items():
            if f == N:
                possible.append(num)
        if not possible:
            return -1

        for p in possible:
            temp_min = (
                N - tops.count(p)
                if tops.count(p) > bottoms.count(p)
                else N - bottoms.count(p)
            )

            min_operations = min(min_operations, temp_min)

        return min_operations
