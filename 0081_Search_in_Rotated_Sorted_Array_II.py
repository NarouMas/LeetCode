from msilib.sequence import tables
from operator import le


class Solution:
    def search(self, nums: [int], target: int) -> bool:
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False
        
        left, right = 0, len(nums) - 1
        while left <= right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while right > left and nums[right] == nums[right - 1]:
                right -= 1

            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[left] <= nums[mid]:
                if nums[mid] >= target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target>=nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False

if __name__ == '__main__':
    a = Solution()
    arr = [2,5,6,0,0,1,2]
    print(a.search(arr, 3))
