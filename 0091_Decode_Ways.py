class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        fi = [1] * 64
        for i in range(2, 64):
            fi[i] = fi[i - 1] + fi[i - 2]
        ans = 1
        i = 0
        count = 0
        while i < len(s):
            count += 1
            cut = True
            if i != len(s) - 1:
                if s[i] == '1':
                    cut = False
                elif s[i] == '2' and ord(s[i + 1]) - 48 <= 6:
                    cut = False
            if cut:
                if s[i] == '0' and count == 1:
                    return 0
                elif s[i] == '0':
                    count -= 2
                ans *= fi[count]
                count = 0
            i += 1
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.numDecodings("21130135"))