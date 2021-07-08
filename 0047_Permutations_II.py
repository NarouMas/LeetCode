from collections import Counter


class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        ans = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                ans.append(list(comb))
                return
            for i in counter:
                if counter[i] > 0:
                    comb.append(i)
                    counter[i] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[i] += 1

        backtrack([], Counter(nums))
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.permuteUnique([1, 1, 2]))

