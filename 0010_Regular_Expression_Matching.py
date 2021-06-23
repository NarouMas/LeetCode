import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = re.match(p, s)
        if result is None:
            return False
        result = result.group()
        return True if len(result) == len(s) else False


if __name__ == '__main__':
    a = Solution()
    print(a.isMatch('mississippi', 'ab'))
