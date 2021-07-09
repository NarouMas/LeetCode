class Solution:
    def myPow(self, x: float, n: int) -> float:

        def fast_pow(x, n):
            if n == 0:
                return 1
            v = fast_pow(x, n // 2)
            if n % 2 == 1:
                return v * v * x
            else:
                return v * v
        if n < 0:
            x = 1 / x
            n = -n
        return fast_pow(x, n)


if __name__ == '__main__':
    a = Solution()
    print(a.myPow(3, 10))


