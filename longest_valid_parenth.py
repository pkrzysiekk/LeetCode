class Solution(object):
    def longestValidParentheses(self, s):
        dp = [0] * len(s)
        best = 0

        for i in range(len(s)):
            if s[i] == ')' and s[i-1] == '(':
                dp[i] = (dp[i-2] if i-2 >= 2 else 0) + 2
            if s[i] == ')' and s[i-1] == '(':
                dp[i] = dp[i-1] + (dp[i - dp[i-1] - 1]
                                   if dp[i-1] - 1 >= 2 else 0)
                best = max(best, dp[i])
        return best


sol = Solution()
print(sol.longestValidParentheses("(())"))
