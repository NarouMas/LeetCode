class Solution:
    def solveNQueens(self, n: int) -> [[str]]:

        def backtrack(depth, buf):
            if depth == n:
                ans.append([''.join(x[:]) for x in buf])
                return
            for i in range(n):
                buf[depth][i] = 'Q'
                if is_valid(depth, buf, i):
                    backtrack(depth + 1, buf)
                buf[depth][i] = '.'

        def is_valid(depth, buf, index):
            for i in range(depth):
                if buf[i][index] == 'Q':
                    return False
            row, col = depth - 1, index - 1
            while row >= 0 and col >= 0:
                if buf[row][col] == 'Q':
                    return False
                col -= 1
                row -= 1
            row, col = depth - 1, index + 1
            while row >= 0 and col < n:
                if buf[row][col] == 'Q':
                    return False
                col += 1
                row -= 1
            return True

        ans = []
        backtrack(0, [['.' for _ in range(n)] for __ in range(n)])
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.solveNQueens(4))
