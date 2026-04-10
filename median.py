
def merge(nums1, nums2):
    i = 0
    j = 0
    n = len(nums1)
    m = len(nums2)
    arr = []
    while i < n and j < m:
        if nums1[i] < nums2[i]:
            arr.append(nums1[i])
            i += 1
        else:
            arr.append(nums2[j])
            j += 1

    while i < n:
        arr.append(nums1[i])
        i += 1
    while j < m:
        arr.append(nums2[j])
        j += 1
    return arr


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr = merge(nums1, nums2)
        n = len(arr)

        if n % 2 == 0:
            return (arr[n//2 - 1] + arr[n//2])/2.0
        else:
            return arr[n//2]


def main():
    sol = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(sol.findMedianSortedArrays(nums1, nums2))


main()
