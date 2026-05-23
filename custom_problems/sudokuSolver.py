class Solution(object):
    def isValid(self, grid, r, c, k):
        not_in_row = k not in grid[r]
        if not not_in_row:
            return False
        not_in_col = k not in [grid[i][c] for i in range(9)]
        if not not_in_col:
            return False
        not_in_box = k not in [grid[i][j] for i in range(
            r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)]
        if not not_in_box:
            return False
        return True

    def solve(self, board, r, c):
        if r == 9:
            return True
        elif c == 9:
            return self.solve(board, r+1, 0)
        elif board[r][c] != ".":
            return self.solve(board, r, c+1)
        else:
            for k in range(1, 10):
                if self.isValid(board, r, c, str(k)):
                    board[r][c] = str(k)
                    if self.solve(board, r, c+1):
                        return True
                    board[r][c] = "."
            return False

    def solveSudoku(self, board):
        self.solve(board, 0, 0)
