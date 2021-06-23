class Solution:
    def intToRoman(self, num: int) -> str:
        ch = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = ''
        for i in range(len(value)):
            while num >= value[i]:
                ans += ch[i]
                num -= value[i]
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.intToRoman(1994))
