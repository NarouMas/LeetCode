import math

class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(math.ceil(n / 2)):
            for j in range(n - i * 2 - 1):

                temp = matrix[i][j + i]
                matrix[i][j + i] = matrix[n - 1 - i - j][i]
                matrix[n - 1 - i - j][i] = matrix[n - 1 - i][n - 1 - i - j]
                matrix[n - 1 - i][n - 1 - i - j] = matrix[j + i][n - 1 - i]
                matrix[j + i][n - 1 - i] = temp

        return


if __name__ == '__main__':
    # print(i, j)
    # print('(' + str(i) + ',' + str(j + i) + '), ' + '(' + str(n - 1 - i - j) + ',' + str(i) + '), ' +
    #       '(' + str(n - 1 - i) + ',' + str(n - 1 - i - j) + '), ' + '(' + str(j) + ',' + str(n - 1 - i) + ')')
    arr = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    a = Solution()
    a.rotate(arr)
    print(arr)
