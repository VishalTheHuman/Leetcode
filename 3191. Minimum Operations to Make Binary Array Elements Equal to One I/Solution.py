class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for idx,x in enumerate(nums[:-2]):
            if not nums[idx]:
                count += 1
                for i in range(idx,idx+3):
                    nums[i] = not nums[i]
        
                    
        return -1 if sum(nums)!=len(nums) else count
