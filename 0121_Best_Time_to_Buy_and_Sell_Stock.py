class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        low = prices[0]
        for v in prices:
            low = min(low, v)
            ans = max(ans, v - low)
        return ans

if __name__ == '__main__':
    a = Solution()
    print(a.maxProfit([7]))