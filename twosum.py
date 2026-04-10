class Solution(object):
    def twoSum(self, nums:list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = dict()
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in map:
                return [i,map.get(comp)]
            map[nums[i]]=i


                
 
sol = Solution()
nums = [2,7,11,15]

target = 9
print(sol.twoSum(nums=nums,target=target))

        
 