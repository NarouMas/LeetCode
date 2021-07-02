class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        for i in range(9):
            dic = {}
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in dic:
                    return False
                dic[board[i][j]] = True
        for i in range(9):
            dic = {}
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] in dic:
                    return False
                dic[board[j][i]] = True
        for i in range(9):
            dic = {}
            for j in range(9):
                row = int(j / 3) + int(i / 3) * 3
                col = j % 3 + (i % 3) * 3
                if board[row][col] == '.':
                    continue
                elif board[row][col] in dic:
                    return False
                dic[board[row][col]] = True

        return True


if __name__ == '__main__':
    a = Solution()
    print(a.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                              , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                              , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                              , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                              , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                              , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                              , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                              , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                              , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
