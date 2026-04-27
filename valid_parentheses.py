class Solution(object):
    def isValid(self, s):
        openning = {'(', '{', '['}
        stack = []

        for char in s:
            if char in openning:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if curr == '(' and char == ')':
                    continue
                elif curr == '{' and char == '}':
                    continue
                elif curr == '[' and char == ']':
                    continue
                return False
        return True if len(stack) == 0 else False


sol = Solution()
s = "["
print(sol.isValid(s))
