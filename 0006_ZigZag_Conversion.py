class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = 1
        ans = ''
        if numRows > 1:
            n = (numRows - 1) << 1
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                for j in range(i, len(s), n):
                    ans += s[j]
            else:
                j = i
                stat = True
                while j < len(s):
                    ans += s[j]
                    if stat:
                        j += (numRows - 1 - i) << 1
                        stat = False
                    else:
                        j += i << 1
                        stat = True

        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.convert('abcdefghijklmnopqrstuvwxyz', 5))  # aiqybhjprxzcgkoswdflntvemu
