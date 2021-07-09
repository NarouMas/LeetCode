from collections import Counter


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        ans = {}
        for i in range(len(strs)):
            word = ''.join((sorted(strs[i])))
            if word not in ans:
                ans[word] = [strs[i]]
            else:
                ans[word].append(strs[i])
        return ans.values()


if __name__ == '__main__':
    a = Solution()
    print(a.groupAnagrams(["ddddddddddg", "dgggggggggg"]))
