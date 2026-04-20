class Solution(object):
    def maxArea(self, height):
        n = len(height)
        i = 0
        j = n-1
        best = 0
        while i < j:
            dist = abs(j-i)
            area = 0
            if height[i] < height[j]:
                area = height[i] * dist
                i += 1
            else:
                area = height[j] * dist
                j -= 1
            best = max(best, area)
        return best


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
sol = Solution()
print(sol.maxArea(height))
