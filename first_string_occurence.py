class Solution(object):
    def strStr(self, haystack, needle):
        idx = -1

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                idx = i
                j = 0
                while j < len(needle) and i + j < len(haystack):
                    if haystack[i + j] != needle[j]:
                        break
                    j += 1
                if j < len(needle):
                    idx = -1
                else:
                    return idx
        return idx


haystack = "mississippi"
needle = "issip"

sol = Solution()
print(sol.strStr(haystack, needle))
