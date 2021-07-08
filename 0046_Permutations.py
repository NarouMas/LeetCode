class Solution:
    def permute(self, nums: [int]) -> [[int]]:

        def foo(num, ans, buf):
            if len(buf) == len(num):
                ans.append(list(buf))
                return
            for i in range(len(num)):
                if num[i] not in buf:
                    buf.append(num[i])
                    foo(num, ans, buf)
                    buf.pop()

        res = []
        foo(nums, res, [])
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.permute([0, 1, 2, 3, 4, 5]))
