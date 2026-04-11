import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x

        while low <= high:
            partitionX = (low+high)//2
            partitionY = (x+y+1)//2 - partitionX

            maxLeftX = - \
                math.inf if partitionX == 0 else nums1[partitionX - 1]
            minRightX = math.inf if partitionX == x else nums1[partitionX]

            maxLeftY = - \
                math.inf if partitionY == 0 else nums2[partitionY - 1]
            minRightY = math.inf if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x+y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1


def main():
    nums1 = [1, 3]
    nums2 = [2]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))


main()
