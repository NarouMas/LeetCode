class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        ans = []
        n = len(nums)

        def foo(index, curr):
            ans.append(curr.copy())
            for i in range(index, n):
                curr.append(nums[i])
                foo(i + 1, curr)
                curr.pop()

        foo(0, [])
        return ans

if __name__ == '__main__':
    a = Solution()
    print(a.subsets([0]))
