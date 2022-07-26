from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        @cache
        def foo(i, j):
            if not i or not j:
                return i or j
            if word1[i - 1] == word2[j - 1]:
                return foo(i - 1, j - 1)
            return 1 + min(foo(i - 1, j), foo(i, j - 1), foo(i - 1, j - 1))

        return foo(n, m)


if __name__ == '__main__':
    a = Solution()
    print("ans:", a.minDistance('horse', 'hello'))
