class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == '__main__':
    a = Solution()
    print(a.strStr('hello', 'll'))
    print(a.strStr('aaaaa', 'bba'))
    print(a.strStr('ddd', ''))
