class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        indexA = indexB = 0
        merge = []
        n = len(nums1) + len(nums2)
        for i in range(int(n/2) + 1):
            if indexA < len(nums1) and indexB < len(nums2):
                if nums1[indexA] < nums2[indexB]:
                    merge.append(nums1[indexA])
                    indexA += 1
                else:
                    merge.append(nums2[indexB])
                    indexB += 1
            elif indexA < len(nums1):
                merge.append(nums1[indexA])
                indexA += 1
            elif indexB < len(nums2):
                merge.append(nums2[indexB])
                indexB += 1
        if n % 2 == 1:
            return merge[-1]
        else:
            return (merge[-1] + merge[-2]) / 2


if __name__ == '__main__':
    a = Solution()
    print(a.findMedianSortedArrays([1, 5, 7, 10, 12, 15], [2, 9, 18]))
    print(a.findMedianSortedArrays([1, 5, 7, 10, 12, 15], [2, 9]))
    print(a.findMedianSortedArrays([0], [0]))
