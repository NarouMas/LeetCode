class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        if s is None or words is None:
            return []
        n = len(words)
        m = len(words[0])
        ans = []
        dic = {}
        for i in words:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        for i in range(len(s) - n * m + 1):
            copy = dic.copy()
            k = n
            j = i
            while k > 0:
                st = s[j:j+m]
                if st not in copy or copy[st] < 1:
                    break
                copy[st] -= 1
                k -= 1
                j += m
            if k == 0:
                ans.append(i)
        return ans


if __name__ == '__main__':
    a = Solution()
    print(a.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
