class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i


if __name__ == '__main__':
    a = Solution()
    arr = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(a.removeDuplicates(arr))
    print(arr)
