class Solution(object):
    def isPalindrome(self, x):
        if not x:
            return True
        copy = x
        reversed = 0
        while x > 0:
            reversed = (reversed * 10) + x % 10
            x //= 10
        return reversed == copy


sol = Solution()
print(sol.isPalindrome(121))
