class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1

        if target > nums[r]:
            return r + 1
        if target < nums[l]:
            return 0

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if target < nums[l]:
            return l - 1
        else:
            return r + 1


nums = [1, 3, 5, 6]
target = 7
sol = Solution()
print(sol.searchInsert(nums, target))
