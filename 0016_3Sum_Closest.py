class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        n = len(nums)
        nums.sort()
        diff = 2147483647
        for i, v in enumerate(nums):
            lo = i + 1
            hi = n - 1
            while hi > lo:
                total = v + nums[lo] + nums[hi]
                # print(v, nums[lo], nums[hi], total)
                if abs(total - target) < abs(diff):
                    diff = target - total
                    # print(diff)
                    if diff == 0:
                        break
                if total < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff


if __name__ == '__main__':
    a = Solution()
    print(a.threeSumClosest([1, 1, -1, -1, 3], -1))
