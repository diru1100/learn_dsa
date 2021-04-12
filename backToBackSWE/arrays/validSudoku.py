class Solution:
    def checkSubMatrix(self, row_index, col_index, board):

        start_sub_matrix_row_index = row_index - (row_index % 3)
        start_sub_matrix_col_index = col_index - (col_index % 3)
        end_sub_matrix_row_index = row_index + (3 - (row_index % 3)) - 1
        end_sub_matrix_col_index = col_index + (3 - (col_index % 3)) - 1

        num_to_check = board[row_index][col_index]

        for i in range(start_sub_matrix_row_index, end_sub_matrix_row_index + 1):
            for j in range(start_sub_matrix_col_index, end_sub_matrix_col_index + 1):
                if i == row_index and j == col_index:
                    continue

                if board[i][j] == 0:
                    continue

                if num_to_check == board[i][j]:
                    return False

        return True

    def checkRowCol(self, row_index, col_index, board):
        num_to_check = board[row_index][col_index]

        for j in range(0, 9):
            if j == col_index:
                continue
            if num_to_check == board[row_index][j]:
                return False

        for j in range(0, 9):
            if j == row_index:
                continue
            if num_to_check == board[j][col_index]:
                return False

        return True

    def validSudoku(self, board):
        """
        :type board: list of list of int
        :rtype: bool
        """
        # print(board)
        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == 0:
                    continue

                if self.checkRowCol(row, col, board) and self.checkSubMatrix(
                    row, col, board
                ):
                    continue
                else:
                    print(row)
                    print(col)
                    return False

        return True


s = Solution()
print(
    s.validSudoku(
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
    )
)
