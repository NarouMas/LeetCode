class Solution:
    def search(self, nums: [int], target: int) -> int:
        rotate = self.find_rotate(nums)
        if nums[rotate] == target:
            return rotate
        elif rotate == 0:
            ans = self.binary_search(nums, 0, len(nums) - 1, target)
        elif target >= nums[0]:
            ans = self.binary_search(nums, 0, rotate - 1, target)
        else:
            ans = self.binary_search(nums, rotate, len(nums) - 1, target)
        return ans

    def find_rotate(self, nums):
        head, tail = 0, len(nums) - 1
        while tail > head and nums[tail] > nums[tail - 1]:
            mid = int((tail + head) / 2)
            if nums[mid] > nums[tail]:
                head = mid
            else:
                tail = mid
        return tail

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
    print(a.search([1], 1))
