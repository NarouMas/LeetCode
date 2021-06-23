class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None or x < 0:
            return False
        x = str(x)
        center = int(len(x) / 2)
        if len(x) % 2 == 0:
            le = self.expandCenter(x, center - 1, center)
        else:
            le = self.expandCenter(x, center, center)
        if le == len(x):
            return True
        return False

    def expandCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


if __name__ == '__main__':
    a = Solution()
    print(a.isPalindrome(1234321))
