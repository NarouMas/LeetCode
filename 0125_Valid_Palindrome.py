import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ', '')
        s = s.translate(str.maketrans('', '', string.punctuation))
        return s == s[::-1]


if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome("0P"))