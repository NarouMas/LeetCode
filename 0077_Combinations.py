class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        ans = []
        if k == 1:
            for i in range(1, n + 1):
                ans.append([i])
            return ans

        def foo(l):
            if len(l) == k:
                ans.append(l.copy())
            for i in range(l[-1] + 1, n + 1):
                l.append(i)
                foo(l)
                l.pop()
        for num in range(1, n):
            foo([num])

        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.combine(1, 1))
