class Solution(object):
    def convert(self, s, numRows):
        if numRows <= 1:
            return s

        idx = 0
        d = 0
        rows = [[] for _ in range(numRows)]
        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d
        for i in range(numRows):
            rows[i] = "".join(rows[i])

        return "".join(rows)


sol = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(sol.convert(s, numRows))
