class Solution:
    def isNumber(self, s: str) -> bool:
        num = False
        numAfterE = True
        dot = False
        exp = False
        sign = False
        n = len(s)
        for i in range(n):
            if s[i] == ' ':
                if i < n - 1 and s[i + 1] != ' ' and (num or dot or exp or sign):
                    return False
            elif s[i] == '+' or s[i] == '-':
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != ' ':
                    return False
                sign = True
            elif ord('0') <= ord(s[i]) <= ord('9'):
                num = True
                numAfterE = True
            elif s[i] == '.':
                if dot or exp:
                    return False
                dot = True
            elif s[i] == 'e' or s[i] == 'E':
                if exp or not num:
                    return False
                exp = True
                numAfterE = False
            else:
                return False
        return num and numAfterE


def main():
    a = Solution()
    test = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    for s in test:
        print(a.isNumber(s))
    print('False start')
    test = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    for s in test:
        print(a.isNumber(s))


if __name__ == '__main__':
    main()
