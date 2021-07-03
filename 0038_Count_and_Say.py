class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for i in range(n - 1):
            temp = ''
            count, j = 1, 1
            while j <= len(ans):
                while len(ans) > j > 0 and ans[j] == ans[j - 1]:
                    count += 1
                    j += 1
                temp += str(count) + ans[j - 1]
                j += 1
                count = 1
            ans = temp
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.countAndSay(1))
