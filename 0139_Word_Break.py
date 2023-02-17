class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        word_set = set(wordDict)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]

if __name__ == "__main__":
    a = Solution()
    print(a.wordBreak("leetcode", ["leet", "code"]))