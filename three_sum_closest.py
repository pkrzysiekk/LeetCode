import math


class Solution(object):
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        closest = math.inf
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            lo = i+1
            hi = n-1
            if i > 0 and nums[i] == nums[i - 1]:
                lo += 1
                continue
            while lo < hi:
                curr_sum = curr + nums[lo] + nums[hi]
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                elif curr_sum < target:
                    lo += 1
                elif curr_sum > target:
                    hi -= 1
                else:
                    return target
        return closest


sol = Solution()
nums = [-1000, -1000, -1000]

target = 10000
print(sol.threeSumClosest(nums, target))
