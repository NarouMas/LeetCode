class Solution:
    def romanToInt(self, s: str) -> int:
        ch = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = i = j = 0
        stat = True
        while i < len(s):
            if stat:
                if s[i] == ch[j]:
                    ans += value[j]
                else:
                    j += 1
                    i -= 1
                    stat = False
            else:
                if i != len(s) - 1 and s[i] + s[i + 1] == ch[j]:
                    ans += value[j]
                    i += 1
                else:
                    j += 1
                    i -= 1
                    stat = True
            i += 1
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.romanToInt('MCMXCIV'))
