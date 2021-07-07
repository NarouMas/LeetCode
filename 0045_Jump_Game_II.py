class Solution:
    def jump(self, nums: [int]) -> int:
        step = 0
        near = 0
        far = 0
        for i in range(len(nums)):
            if i > near:
                step += 1
                near = far
            far = max(far, nums[i] + i)
        return step


if __name__ == '__main__':
    a = Solution()
    print(a.jump([2, 3, 0, 1, 4]))
