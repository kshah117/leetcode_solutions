class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COL = len(board[0])
        safe = set()
        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(r, c):
            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COL
                or board[r][c] == "X"
                or (r, c) in visited
            ):
                return

            visited.add((r, c))
            safe.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for i in range(ROWS):
            for j in range(COL):
                if (i, j) in safe:
                    continue
                if (i in [0, ROWS - 1] or j in [0, COL - 1]) and board[i][j] == "O":
                    dfs(i, j)

        for i in range(ROWS):
            for j in range(COL):
                if board[i][j] == "O" and (i, j) not in safe:
                    board[i][j] = "X"
