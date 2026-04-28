class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        i = 0
        j = 0
        best = 0

        while j < len(nums):
            if nums[j] == 1:
                j += 1
                best = max(best, j-i)
            else:
                i = j + 1
                j += 1
        return best


sol = Solution()

nums = [1, 1, 0, 1, 1, 1]
print(sol.findMaxConsecutiveOnes(nums))
