class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = int(dividend / divisor)
        if ans > 2147483647 or ans < -2147483648:
            return 2147483647
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.divide(-2147483648, -1))
