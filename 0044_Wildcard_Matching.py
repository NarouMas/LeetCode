class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sp = pp = match = 0
        star = -1
        while sp < len(s):
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
            elif pp < len(p) and p[pp] == '*':
                star = pp
                match = sp
                pp += 1
            elif star != -1:
                pp = star + 1
                match += 1
                sp = match
            else:
                return False
        while pp < len(p) and p[pp] == '*':
            pp += 1
        return pp == len(p)


if __name__ == '__main__':
    a = Solution()
    print(a.isMatch("aa", "a"))
