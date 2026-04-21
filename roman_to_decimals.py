class Solution(object):
    def romanToInt(self, s):
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        j = n-1
        res = 0
        while j >= 0:
            if roman_map[s[j]] <= roman_map[s[j-1]]:
                res += roman_map[s[j]]
                j -= 1
            elif j == 0:
                res += roman_map[s[j]]
                j -= 1
            else:
                res += roman_map[s[j]] - roman_map[s[j-1]]
                j -= 2
        return res


sol = Solution()
s = "IV"
print(sol.romanToInt(s))
