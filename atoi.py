class Solution(object):
    def myAtoi(self, s):

        number = 0
        is_negative = False
        idx = 0
        n = len(s)
        while idx < n and s[idx] == " ":
            idx += 1
        if idx == n:
            return number
        if s[idx] == "-":
            is_negative = True
            idx += 1
        elif s[idx] == "+":
            idx += 1
        while idx < n and s[idx] == "0":
            idx += 1
        while idx < n:
            char = s[idx]
            if char.isnumeric():
                number = (number * 10) + int(char)
                idx += 1
            if number > 2**31 - 1:
                return (-2) ** 31 if is_negative else 2**31 - 1
            elif idx == n or not char.isnumeric():
                break
        return number * (-1) if is_negative else number


s = "-+12"


sol = Solution()
print(sol.myAtoi(s))
