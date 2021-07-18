class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        carry = 0
        res = ''
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                res += '1'
            else:
                res += '0'
            carry = carry // 2
        if carry == 1:
            res += '1'
        return res[::-1]



if __name__ == '__main__':
    a = Solution()
    print(a.addBinary("11000", "10100"))
