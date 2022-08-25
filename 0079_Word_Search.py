class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        used = [[False] * n for _ in range(m)]

        def find(index, y, x):
            if index == len(word):
                return True
            used[y][x] = True
            if x > 0 and not(used[y][x - 1]) and board[y][x - 1] == word[index]:
                if find(index + 1, y, x - 1):
                    return True
            if y > 0 and not(used[y - 1][x]) and board[y - 1][x] == word[index]:
                if find(index + 1, y - 1, x):
                    return True
            if x < n - 1 and not(used[y][x + 1]) and board[y][x + 1] == word[index]:
                if find(index + 1, y, x + 1):
                    return True
            if y < m - 1 and not(used[y + 1][x]) and board[y + 1][x] == word[index]:
                if find(index + 1, y + 1, x):
                    return True
            used[y][x] = False
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if find(1, i, j):
                        return True

        return False


if __name__ == '__main__':
    a = Solution()
    print(a.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCEDASA"))
