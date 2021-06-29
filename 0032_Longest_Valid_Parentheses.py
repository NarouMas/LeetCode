class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s is None:
            return 0
        dp = [0 for _ in range(len(s))]
        ans = 0
        for i in range(1, len(s)):
            if s[i] == '(':
                continue
            elif s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2 if i >= 2 else 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
            ans = max(ans, dp[i])
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.longestValidParentheses('())()((()))((()'))
