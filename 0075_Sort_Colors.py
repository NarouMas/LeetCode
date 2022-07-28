class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for _ in range(len(nums)):
            if nums[index] == 0:
                nums.pop(index)
                nums.insert(0, 0)
                index += 1
            elif nums[index] == 2:
                nums.pop(index)
                nums.append(2)
            else:
                index += 1


if __name__ == '__main__':
    a = Solution()
    l = [2, 0, 1]
    a.sortColors(l)
    for i in range(len(l)):
        print(l[i], end=' ')
