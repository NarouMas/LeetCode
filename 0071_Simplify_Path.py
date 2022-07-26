class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        dic = []
        for p in paths:
            if p == '' or p == '.':
                continue
            elif p == '..':
                dic = dic[:-1]
            else:
                dic.append(p)
        return '/' + '/'.join(dic)


if __name__ == '__main__':
    a = Solution()
    print("ans:", a.simplifyPath('/../'))

