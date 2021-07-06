class Solution:
    def trap(self, height: [int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.trap([4, 2, 0, 3, 2, 5]))
