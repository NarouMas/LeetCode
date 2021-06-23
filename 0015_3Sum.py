class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            dic = {}
            target = v * -1
            for j in range(i + 1, n):
                if target - nums[j] in dic:
                    ans.add((v, target - nums[j], nums[j]))
                dic[nums[j]] = nums[j]
        return list(ans)



if __name__ == '__main__':
    a = Solution()
    print(a.threeSum([-1, 0, 1, 2, -1, -4]))
