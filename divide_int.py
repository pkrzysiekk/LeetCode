class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        d = abs(dividend)
        dv = abs(divisor)
        res = 0
        while d >= dv:
            pow = 0
            while d >= dv << (pow+1):
                pow += 1
            res += 1 << pow
            d = d - (dv << pow)

        is_neg = (dividend > 0 and divisor < 0) or (
            dividend < 0 and divisor > 0)

        if res > INT_MAX and not is_neg:
            return INT_MAX
        if res > INT_MAX and is_neg:
            return INT_MIN
        if is_neg:
            res = - res
        return res


sol = Solution()
dividend = 10
divisor = -2
print(sol.divide(dividend, divisor))
