class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] > n or nums[i] <= 0 or nums[i] == i + 1 or nums[nums[i] - 1] == nums[i]:
                i += 1
                continue
            self.swap(nums, i, nums[i] - 1)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp


if __name__ == '__main__':
    a = Solution()
    print(a.firstMissingPositive([8, -1, 2, 3]))
