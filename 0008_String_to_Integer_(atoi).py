class Solution:
    def myAtoi(self, s: str) -> int:
        hasNumber = False
        if s is None or len(s) < 1:
            return 0
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            if self.isNumber(s[i]):
                s = s[i:]
                hasNumber = True
                break
            return 0
        if not hasNumber:
            return 0
        for i in range(len(s)):
            if s[i].isdigit() or ((s[i] == '-' or s[i] == '+') and i == 0):
                continue
            s = s[:i]
            break
        if len(s) == 1 and (s == '-' or s == '+'):
            return 0
        ans = int(s)
        if ans >= 2147483647:
            return 2147483647
        if ans <= -2147483648:
            return -2147483648
        return ans

    def isNumber(self, c):
        if 0 <= ord(c) - 48 <= 9 or (c == '-' or c == '+'):
            return True
        return False


if __name__ == '__main__':
    a = Solution()
    print(a.myAtoi(''))
