class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        dic = {}
        for i in range(len(nums)):
            if dic.__contains__(target - nums[i]):
                return [dic.get(target-nums[i]), i]
            else:
                dic[nums[i]] = i

if __name__ == '__main__':
    a = Solution()
    print(a.twoSum([1, 2, 7, 8, 4], 15))

