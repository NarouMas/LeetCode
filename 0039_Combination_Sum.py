class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        ans = []
        self.foo(candidates, target, 0, 0, ans, [])
        return ans

    def foo(self, nums, target, index, total, ans, buf):
        if total == target:
            ans.append(buf[:])
            return
        for i in range(index, len(nums)):
            if total + nums[i] <= target:
                buf.append(nums[i])
                self.foo(nums, target, i, total + nums[i], ans, buf)
                buf.pop()


if __name__ == '__main__':
    a = Solution()
    print(a.combinationSum([2, 5], 30))
