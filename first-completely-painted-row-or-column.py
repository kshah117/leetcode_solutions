class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        M = len(mat)
        N = len(mat[0])
        pos = {}
        for r in range(M):
            for c in range(N):
                pos[mat[r][c]] = (r, c)

        rows = [0] * M
        cols = [0] * N

        for i in range(len(arr)):
            r, c = pos[arr[i]]
            rows[r] += 1
            cols[c] += 1

            if rows[r] == N or cols[c] == M:
                return i
