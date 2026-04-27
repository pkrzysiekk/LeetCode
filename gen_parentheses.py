class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def backtrack(currString, open, closed):
            if open == n and closed == n:
                res.append(currString)
                return
            if closed < open:
                backtrack(currString+')', open, closed+1)
            if open < n:
                backtrack(currString+'(', open+1, closed)

        if n > 0:
            backtrack("", 0, 0)
        return res


sol = Solution()
n = 20
print(sol.generateParenthesis(n))
