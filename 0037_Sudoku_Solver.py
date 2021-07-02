class Solution:
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solver(board, 0, 0)

    def solver(self, board, i, j):
        if i == 9:
            return True
        elif j >= 9:
            return self.solver(board, i + 1, 0)
        elif board[i][j] != '.':
            return self.solver(board, i, j + 1)
        else:
            for val in self.number:
                if not self.is_valid(board, i, j, val):
                    continue
                board[i][j] = val
                if self.solver(board, i, j + 1):
                    return True
                board[i][j] = '.'
        return False

    def is_valid(self, board, row, col, val):
        for i in range(9):
            if board[row][i] == val:
                return False
        for i in range(9):
            if board[i][col] == val:
                return False
        r = row - row % 3
        c = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + r][j + c] == val:
                    return False
        return True


if __name__ == '__main__':
    a = Solution()
    sudoku = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    a.solveSudoku(sudoku)
    print(sudoku)
