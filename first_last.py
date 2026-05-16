class Solution(object):
    def searchRange(self, nums, target):

        def binary_search(nums, target, is_searching_left):
            l = 0
            r = len(nums) - 1
            idx = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    idx = mid
                    if is_searching_left:
                        r = mid - 1
                    else:
                        l = mid + 1
            return idx
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        return [left, right]


sol = Solution()
nums = [3, 3, 3]
print(sol.searchRange(nums, 3))
