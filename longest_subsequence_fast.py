class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        max_length=0
        i=0
        j=0
        hash_set=set()

        while j < n:
            if  s[j] not in hash_set:
                hash_set.add(s[j])
                j+=1
                max_length=max(max_length,j-i) 
            else:
                hash_set.remove(s[i])
                i+=1
        return max_length
def main():
    sol=Solution()
    s = "abbb"
    print(sol.lengthOfLongestSubstring(s))
main()
        




            




