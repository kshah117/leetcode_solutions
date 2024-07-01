from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_rows():
            for r in range(9):
                row = []
                for c in range(9):
                    if board[r][c] == '.':
                        continue
                    if not board[r][c] in row:
                        row.append(board[r][c])
                    else:
                        return False

            return True

        def check_columns():
            for c in range(9):
                col = []
                for r in range(9):
                    if board[r][c] == '.':
                        continue
                    if not board[r][c] in col:
                        col.append(board[r][c])
                    else:
                        return False
            return True

        def check_boxes():
            boxes = {}
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        continue
                    if boxes.get((r // 3, c // 3)):
                        if board[r][c] not in boxes[(r // 3, c // 3)]:
                            boxes[(r // 3, c // 3)].append(board[r][c])
                        else:
                            return False
                    else:
                        boxes[(r // 3, c // 3)] = [board[r][c]]

            return True

        # print(check_rows())
        # print(check_columns())
        # print(check_boxes())
        if check_rows() and check_columns() and check_boxes():
            return True
        else:
            return False


sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board=board))