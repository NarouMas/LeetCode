class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 1
        n -= 1
        m -= 1
        for i in range((m + n), max(m, n), -1):
            ans *= i
        for i in range(1, min(m, n) + 1):
            ans /= i
        return int(ans)


if __name__ == '__main__':
    a = Solution()
    print(a.uniquePaths(2, 2))
