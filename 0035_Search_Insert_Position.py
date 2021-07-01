class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)

    def binary_search(self, nums, head, tail, target):
        while head <= tail:
            mid = int((tail + head) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                head = mid + 1
            else:
                tail = mid - 1
        return tail + 1


if __name__ == '__main__':
    a = Solution()
    print(a.searchInsert([1], 2))
