class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        index = self.binary_search(nums, 0, len(nums) - 1, target)
        left = right = index
        while left > 0 and nums[left - 1] == target:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] == target:
            right += 1
        return [left, right]

    def binary_search(self, nums, head, tail, target):
        while head <= tail:
            mid = int((tail + head) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                head = mid + 1
            else:
                tail = mid - 1
        return -1


if __name__ == '__main__':
    a = Solution()
    print(a.searchRange([5, 5, 5, 7, 7, 8, 8, 10, 10, 10], 10))
