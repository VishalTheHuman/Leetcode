class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for j in range(len(nums)):
            for i in range(j):
                if nums[i]==nums[j]:
                    count+=1
        return count