class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        dp = ans = nums[0]
        for i in range(1, len(nums)):
            if dp < 0:
                dp = nums[i]
            else:
                dp = dp + nums[i]
            ans = max(ans, dp)
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
