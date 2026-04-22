class Solution(object):
    def threeSum(self, nums):
        res = []
        arr = sorted(nums)
        for i, a in enumerate(arr):
            if i > 0 and a == arr[i - 1]:
                continue
            start = i + 1
            end = len(arr)-1
            while start < end:
                sum = a+arr[start] + arr[end]
                if sum == 0:
                    res.append([a, arr[start], arr[end]])
                    start += 1
                    while arr[start] == arr[start - 1] and start < end:
                        start += 1
                elif sum < 0:
                    start += 1
                elif sum > 0:
                    end -= 1
        return res


sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))
