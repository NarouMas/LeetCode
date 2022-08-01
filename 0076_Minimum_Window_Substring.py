from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        ans = float('inf'), 0, 0
        left, right = 0, 0
        dict_t = Counter(t)
        formed = 0
        required = len(dict_t)
        window_count = {}
        filtered_s = []
        for i, v in enumerate(s):
            if v in t:
                filtered_s.append((i, v))
        while right < len(filtered_s):
            character = filtered_s[right][1]
            window_count[character] = window_count.get(character, 0) + 1
            if character in dict_t and window_count[character] == dict_t[character]:
                formed += 1

            while left <= right and formed == required:
                character = filtered_s[left][1]
                if filtered_s[right][0] - filtered_s[left][0] + 1 < ans[0]:
                    ans = (filtered_s[right][0] - filtered_s[left][0] + 1, filtered_s[left][0], filtered_s[right][0])
                window_count[character] -= 1
                if character in dict_t and window_count[character] < dict_t[character]:
                    formed -= 1
                left += 1
            right += 1

        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]


if __name__ == '__main__':
    a = Solution()
    print(a.minWindow('ADOBECODEBANC', 'ABdC'))
