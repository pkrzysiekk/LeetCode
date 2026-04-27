class Solution(object):
    def generateParenthesis(self, n):
        res = []
        curr = []

        def backtrack(currString, open, closed):
            if open == n and closed == n:
                res.append("".join(curr))
                return
            if closed < open:
                curr.append(')')
                backtrack(currString+')', open, closed+1)
                curr.pop()
            if open < n:
                curr.append('(')
                backtrack(currString+'(', open+1, closed)
                curr.pop()

        if n > 0:
            backtrack("", 0, 0)
        return res


sol = Solution()
n = 15
print(sol.generateParenthesis(n))
