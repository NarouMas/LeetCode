class Solution:
    def isValid(self, s: str) -> bool:
        return self.dfs(s, 0, [])

    def dfs(self, s, n, st):
        if n == len(s):
            if len(st) == 0:
                return True
            return False
        if s[n] == '(' or s[n] == '[' or s[n] == '{':
            st.append(s[n])
            return self.dfs(s, n + 1, st)
        else:
            if len(st) == 0:
                return False
            elif s[n] == ')' and st.pop() == '(':
                return self.dfs(s, n + 1, st)
            elif s[n] == ']' and st.pop() == '[':
                return self.dfs(s, n + 1, st)
            elif s[n] == '}' and st.pop() == '{':
                return self.dfs(s, n + 1, st)
            else:
                return False


if __name__ == '__main__':
    a = Solution()
    print(a.isValid('{[]}'))
