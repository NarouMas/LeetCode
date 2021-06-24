class Solution:
    content = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    ans = []

    def letterCombinations(self, digits: str) -> [str]:
        if len(digits) < 1:
            return []
        self.ans = []
        self.dfs(digits, 0, "")
        return self.ans

    def dfs(self, digits, level, out):
        if level == len(digits):
            self.ans.append(out)
            return
        s = self.content[int(digits[level])]
        for i in s:
            self.dfs(digits, level + 1, out + i)



if __name__ == '__main__':
    a = Solution()
    print(a.letterCombinations('23'))
    print(a.letterCombinations('2'))
