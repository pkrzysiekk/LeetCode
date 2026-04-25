class Solution(object):
    def fourSum(self, nums, target):
        res = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            first = i
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                second = j
                third = j+1
                fourth = n-1
                while third < fourth:
                    curr_sum = nums[first] + nums[second] + \
                        nums[third] + nums[fourth]
                    if curr_sum == target:
                        res.append([nums[first], nums[second],
                                   nums[third], nums[fourth]])
                        third += 1
                        while nums[third] == nums[third - 1] and third < fourth:
                            third += 1
                    elif curr_sum < target:
                        third += 1
                    else:
                        fourth -= 1
        return res


sol = Solution()
nums = [-2, -1, -1, 1, 1, 2, 2]

target = 0
print(sol.fourSum(nums, target))
