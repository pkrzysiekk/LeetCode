class Solution(object):
    def letterCombinations(self, digits):
        res = []
        digitToLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, currString):
            if len(currString) == len(digits):
                res.append(currString)
                return
            for c in digitToLetter[digits[i]]:
                backtrack(i+1, currString+c)

        if digits:
            backtrack(0, "")
        return res


sol = Solution()
digits = "23"
print(sol.letterCombinations(digits))
