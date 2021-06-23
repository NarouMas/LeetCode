class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if len(strs) < 1:
            return ''
        if len(strs) == 1:
            return strs[0]
        ans = ''
        j = 0
        done = False
        while not done:
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or j >= len(strs[i - 1]) or strs[i][j] != strs[i - 1][j]:
                    done = True
                    break
            if not done:
                ans += strs[0][j]
            j += 1

        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.longestCommonPrefix(["flower", "flow", "flight"]))
