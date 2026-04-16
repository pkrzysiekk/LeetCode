class Solution(object):
    def myAtoi(self, s):
        if not s:
            return 0
        n = len(s)
        i = 0
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        while i < n and s[i] == " ":
            i += 1

        if n == i:
            return 0
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = (res * 10) + digit
            i += 1

            if sign * res <= MIN_INT:
                return MIN_INT
            elif sign * res >= MAX_INT:
                return MAX_INT

        return res * sign


s = "   -0004"


sol = Solution()
print(sol.myAtoi(s))
