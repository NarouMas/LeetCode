class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            item = matrix[mid // n][mid % n]
            if item == target:
                return True
            elif item > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    a = Solution()
    print(a.searchMatrix([[]], 34))
