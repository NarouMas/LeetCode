class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        n = len(nums)
        cur = 0
        tail = n - 1
        while cur <= tail:
            if nums[cur] == val:
                while tail > cur and nums[tail] == val:
                    tail -= 1
                nums[cur] = nums[tail]
                tail -= 1
            if nums[cur] != val:
                cur += 1
        return cur


if __name__ == '__main__':
    a = Solution()
    arr = [0, 1, 2, 2, 2, 2, 3]
    print(a.removeElement(arr, 2))
    print(arr)
