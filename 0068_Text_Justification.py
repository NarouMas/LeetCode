class Solution:
    def fullJustify(self, words: [str], maxWidth: int) -> [str]:
        res = []
        buf = []
        count = maxWidth
        for i, v in enumerate(words):
            if count - len(v) <= -1:
                tmp = ''
                if len(buf) == 1:
                    tmp += buf[0] + ' ' * (count + 1)
                else:
                    space = count + len(buf)
                    equal_space = space // (len(buf) - 1)
                    unequal_space = space % (len(buf) - 1)
                    for s in buf[:-1]:
                        if unequal_space != 0:
                            tmp += s + ' ' * (equal_space + 1)
                            unequal_space -= 1
                        else:
                            tmp += s + ' ' * equal_space
                    tmp += buf[-1]
                buf = []
                count = maxWidth
                res.append(tmp)

            buf.append(v)
            count -= (len(v) + 1)
        tmp = ''
        for s in buf:
            tmp += s + ' '
        if count > 0:
            tmp += ' ' * count
        if len(tmp) > maxWidth:
            tmp = tmp[:maxWidth]
        res.append(tmp)
        return res




if __name__ == '__main__':
    a = Solution()
    ans = a.fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16)
    for s in ans:
        print(s)
