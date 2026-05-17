class Solution(object):
    def isValidSudoku(self, board):

        for i in range(9):
            visited_x = dict()
            visited_y = dict()
            for j in range(9):
                curr_x = board[i][j]
                curr_y = board[j][i]
                if curr_y in visited_y:
                    return False
                if curr_y not in visited_y and curr_y != '.':
                    visited_y[curr_y] = 1
                if curr_x in visited_x and curr_x != '.':
                    return False
                else:
                    visited_x[curr_x] = 1
        for box_row in range(3):
            for box_col in range(3):
                visited = dict()
                for i in range(3):
                    for j in range(3):
                        row = 3*box_row + i
                        col = 3*box_col + j
                        if board[row][col] == ".":
                            continue
                        curr = board[row][col]
                        if curr in visited:
                            return False
                        else:
                            visited[curr] = 1
        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",
                                                                                                                                                                                                      "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
sol = Solution()
sol.isValidSudoku(board)
