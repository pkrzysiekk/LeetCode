class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        max_substring=0
        for i in range(n):
            hash_set=set()
            local_max=1
            hash_set.add(s[i])
            for j in range(i+1,n):
                if s[j] in hash_set:
                    break
                hash_set.add(s[j]) 
                local_max+=1
            max_substring = max(max_substring,local_max)
        return max_substring

def main():
    sol=Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))
main()
        

