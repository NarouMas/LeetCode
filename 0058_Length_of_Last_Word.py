class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cur = len(s) - 1
        res = 0
        while cur >= 0 and s[cur] == ' ':
            cur -= 1
        while cur >= 0 and s[cur] != ' ':
            cur -= 1
            res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.lengthOfLastWord(" "))
