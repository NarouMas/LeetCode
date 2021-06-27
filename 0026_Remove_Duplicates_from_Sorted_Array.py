class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        k = cur = 1
        while cur < len(nums):
            while cur < len(nums) and nums[cur] == nums[cur - 1]:
                cur += 1
            if cur < len(nums):
                nums[k] = nums[cur]
                k += 1
                cur += 1
        return k


if __name__ == '__main__':
    a = Solution()
    arr = [0, 1, 2, 2, 2, 5, 5, 6, 6, 6, 9]
    print(a.removeDuplicates(arr))
    print(arr)
