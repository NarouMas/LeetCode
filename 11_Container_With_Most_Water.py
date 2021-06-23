class Solution:
    def maxArea(self, height: [int]) -> int:
        if height is None or len(height) < 2:
            return 0
        left = ans = 0
        right = len(height) - 1
        while right != left:
            ans = max(ans, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.maxArea([5, 6, 8]))
