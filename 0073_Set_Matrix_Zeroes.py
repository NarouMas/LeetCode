class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for k in row:
            for i in range(n):
                matrix[k][i] = 0
        for k in col:
            for i in range(m):
                matrix[i][k] = 0


if __name__ == '__main__':
    a = Solution()
    m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print("ans:", a.setZeroes(m))
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=' ')
        print()
