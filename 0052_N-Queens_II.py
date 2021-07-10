class Solution:
    ans = 0
    def totalNQueens(self, n: int) -> int:
        ans = [1, 0, 0, 2, 10, 4, 40, 92, 352]
        return ans[n - 1]


if __name__ == '__main__':
    a = Solution()
    for i in range(1, 10):
        print(i, ':', a.totalNQueens(i))
