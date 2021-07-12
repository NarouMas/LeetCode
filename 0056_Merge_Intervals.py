class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals.sort(key=lambda x: x[0])
        merge = []
        for interval in intervals:
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
                merge[-1][1] = max(merge[-1][1], interval[1])
        return merge


if __name__ == '__main__':
    a = Solution()
    print(a.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
