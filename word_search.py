from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        sp = []
        m = len(board)
        n = len(board[0])

        def helper(gp, cw, covered ):
            if gp in covered:
                print("gp covered", gp)
                return False
            if gp[0] < 0 or gp[0] > m - 1:
                print("m limit", gp)
                return False

            if gp[1] < 0 or gp[1] > n - 1:
                print("n limit", gp)
                return False

            cw += board[gp[0]][gp[1]]
            if cw == word:
                return True

            covered.append(gp)
            print(cw)
            if cw == "cdb":
                print((gp[0], gp[1] - 1), cw)

            if not word.startswith(cw):
                return False

            up = helper((gp[0] - 1, gp[1]), cw, covered.copy())
            if up:
                return True
            down = helper((gp[0] + 1, gp[1]), cw, covered.copy())
            if down:
                return True
            left = helper((gp[0], gp[1] - 1), cw, covered.copy())
            if left:
                return True
            right = helper((gp[0], gp[1] + 1), cw, covered.copy())
            if right:
                return True

            # print("up",up)
            # print("down",down)
            # print("left",left)
            # print("right",right)

            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    sp.append((i, j))

        for x in sp:
            print("New start", x)
            is_word = helper(x, '',[])
            if is_word:
                return True

        return False


sol = Solution()
sol.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB")