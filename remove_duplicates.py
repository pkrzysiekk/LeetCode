class Solution(object):
    def removeDuplicates(self, nums):

        k = 1
        i = 1
        j = 1
        while j < len(nums):
            if nums[j] == nums[i-1]:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                k += 1
        return k, nums


sol = Solution()
nums = [1, 1, 2]
print(sol.removeDuplicates(nums))
