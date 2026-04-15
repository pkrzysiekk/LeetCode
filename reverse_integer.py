class Solution(object):
    def reverse(self, x: int):

        arr = [""]*32
        idx = 0

        number_str = list(str(x))
        if len(number_str) > 32:
            return 0
        j = len(number_str) - 1
        if number_str[0] == '-':
            arr[0] = "-"
            idx += 1
        while number_str[j] != "" and number_str[j] != "-" and j >= 0:
            arr[idx] = number_str[j]
            idx += 1
            j -= 1
        string = "".join(arr)
        number = int(string)
        if number > 2**31-1 or number < -2**31:
            return 0
        return number


sol = Solution()
print(sol.reverse(-123))
