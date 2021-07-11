class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        m, n = len(matrix), len(matrix[0])
        ans = [0 for _ in range(m * n)]
        r = index = 0
        c = -1
        m -= 1
        count_r, count_c = m, n
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(len(matrix) * len(matrix[0])):
            r += direction[index][0]
            c += direction[index][1]
            ans[i] = matrix[r][c]
            if index % 2 == 0:
                count_c -= 1
                if count_c == 0:
                    n -= 1
                    count_c = n
                    index = (index + 1) % 4
            else:
                count_r -= 1
                if count_r == 0:
                    m -= 1
                    count_r = m
                    index = (index + 1) % 4
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
