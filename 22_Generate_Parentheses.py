class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        ans = []

        def foo(s=[], left=0, right=0):
            if len(s) == 2 * n:
                ans.append(''.join(s))
            if left < n:
                s.append('(')
                foo(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(')')
                foo(s, left, right + 1)
                s.pop()
        foo()
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.generateParenthesis(8))
