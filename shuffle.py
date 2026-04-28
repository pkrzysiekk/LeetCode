class Solution(object):
    def shuffle(self, nums, n):

        res = []
        x = []
        y = []
        for i in range(n):
            x.append(nums[i])

        for i in range(n, 2*n):
            y.append(nums[i])

        for i in range(n):
            res.append(x[i])
            res.append(y[i])


sol = Solution()
nums = [2, 5, 1, 3, 4, 7]
n = 3
print(sol.shuffle(nums, 3))
