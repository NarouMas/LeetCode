class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        for i, v in enumerate(nums[:-3]):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                dic = {}
                tar = (v + nums[j] - target) * -1
                for k in range(j + 1, n):
                    if tar - nums[k] in dic:
                        ans.add((v, nums[j], tar - nums[k], nums[k]))
                    dic[nums[k]] = nums[k]
        return list(ans)


if __name__ == '__main__':
    a = Solution()
    print(a.fourSum([1, 0, -1, 0, -2, 2], 3))
    print(a.fourSum([2, 2, 2, 2, 2], 8))
