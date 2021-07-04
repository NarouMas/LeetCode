from collections import Counter


class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        ans = []
        self.foo([], target, 0, counter, ans)
        return list(ans)

    def foo(self, comb, remain, curr, counter, ans):
        if remain == 0:
            ans.append(list(comb))
        elif remain < 0:
            return
        for next_curr in range(curr, len(counter)):
            candidate, freq = counter[next_curr]
            if freq <= 0:
                continue
            comb.append(candidate)
            counter[next_curr] = (candidate, freq - 1)
            self.foo(comb, remain - candidate, next_curr, counter, ans)
            comb.pop()
            counter[next_curr] = (candidate, freq)


if __name__ == '__main__':
    a = Solution()
    print(a.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
