import sys


class Solution(object):
    def freq(self, n):
        res = []
        n = str(n)
        i = 0
        j = 0
        while j < len(n):
            curr = n[i]
            j = i
            count = 0
            while j < len(n) and curr == n[j]:
                j += 1
                count += 1
                i += 1
            res.append([int(curr), count])
        return res

    def combine(self, arr):
        res = ""
        for pair in arr:
            res += str(pair[1]) + str(pair[0])
        return int(res)

    def countAndSay(self, n):
        res = 1
        prev_arr = []
        for i in range(1, n):
            freq_arr = self.freq(res)
            res = self.combine(freq_arr)
        return str(res)


sys.set_int_max_str_digits(10**8)
sol = Solution()
n = 30
print(sol.countAndSay(n))
