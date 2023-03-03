class Solution:
    def moveZeroes(self, nums):
        k=len(nums)
        for x in range(k):
            for y in range(k):
                if nums[x]<nums[y]:
                    u=nums[y]
                    nums[y]=nums[x]
                    nums[x]=u
        i=0
        for x in range(k):
            if nums[x]==0:
                for y in range(k):
                    nums[y]==nums[k-1-i]
                    i+=1
        print(nums)

Solution.moveZeroes(Solution,[0,1,0,3,12])