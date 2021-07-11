class Solution:
    def canJump(self, nums: [int]) -> bool:
        cur = 0
        for i in range(len(nums) - 1):
            if cur < i:
                return False
            elif i + nums[i] > cur:
                cur = i + nums[i]
        return cur >= len(nums) - 1


if __name__ == '__main__':
    a = Solution()
    print(a.canJump([0, 2, 3]))
