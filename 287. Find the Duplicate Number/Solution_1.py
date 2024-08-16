class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ls = [0 for x in range(len(nums)+1)]
        for i in range(len(nums)):
            ls[nums[i]-1]+=1
            if ls[nums[i]-1]>1: 
                return nums[i]
        return -1