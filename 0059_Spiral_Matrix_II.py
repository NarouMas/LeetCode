class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        m = n
        ans = [[0 for _ in range(n)] for _ in range(n)]
        r = index = 0
        c = -1
        m -= 1
        count_r, count_c = m, n
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(1, n * n + 1):
            r += direction[index][0]
            c += direction[index][1]
            ans[r][c] = i
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
    print(a.generateMatrix(3))
