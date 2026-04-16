class Solution(object):
    def isPalindrome(self, x):
        if not x:
            return True

        number = str(x)
        i = 0
        j = len(number) - 1
        while i < j:
            if number[i] != number[j]:
                return False
            i += 1
            j -= 1
        return True


sol = Solution()
print(sol.isPalindrome(""))
