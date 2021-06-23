class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        n = len(s)
        dic = [None] * 128
        for right in range(n):
            if dic[ord(s[right])] is not None:
                left = max(dic[ord(s[right])], left)
            ans = max(right - left + 1, ans)
            dic[ord(s[right])] = right + 1
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.lengthOfLongestSubstring('aa'))
