class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=len(nums)
        count = 0
        for x in range(k):
            if nums[x]==val:
                nums[x]=101
                count+=1
            for y in range(k):
                if nums[x]<nums[y]:
                    temp=nums[x]
                    nums[x]=nums[y]
                    nums[y]=temp
            if nums[x]==val:
                nums[x]=101
                count+=1
        return k - count