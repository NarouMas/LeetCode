class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        ans = 1
        for v in num_set:
            if v - 1 not in num_set:
                count = 1
                while v + 1 in num_set:
                    count += 1
                    v = v + 1
                    ans = max(count, ans)
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))