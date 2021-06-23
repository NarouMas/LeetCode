class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x *= -1
        ans = 0
        carry = 10 ** (len(str(x)) - 1)

        while x > 0:
            ans += (x % 10) * carry
            x = int(x / 10)
            carry /= 10
        if negative:
            ans *= -1
        if ans > 2147483647 or ans < -2147483648:
            return 0
        return int(ans)


if __name__ == '__main__':
    a = Solution()
    print(a.reverse(2123))
