class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        candies = 0
        l2r = [1] * N
        r2l = [1] * N

        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                l2r[i] = l2r[i - 1] + 1

        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                r2l[i] = r2l[i + 1] + 1

        for i in range(N):
            candies += max(l2r[i], r2l[i])

        return candies
