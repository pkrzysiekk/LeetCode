class Solution(object):
    def findErrorNums(self, nums):

        mismatch = []
        all_numbers = {i + 1 for i in range(len(nums))}
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                mismatch.append(nums[i])
            else:
                seen.add(nums[i])
        for number in all_numbers:
            if number not in seen:
                mismatch.append(number)
        return mismatch


sol = Solution()
nums = [1, 2, 2, 4]
print(sol.findErrorNums(nums))
