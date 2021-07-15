class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ''
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        f = [1 for _ in range(n)]
        for i in range(1, n):
            f[i] = f[i - 1] * i
        k -= 1
        for i in range(n - 1, -1, -1):
            j = int(k / f[i])
            k %= f[i]
            ans += num[j]
            num.pop(j)
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.getPermutation(4, 17))
