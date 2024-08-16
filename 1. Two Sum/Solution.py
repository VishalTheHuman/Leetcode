class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {}
        for i in range(len(nums)):
            dt[nums[i]] = i
        
        for i in range(len(nums)):
            if dt.get(target-nums[i],False) and i!=dt[target-nums[i]]:
                return (i,dt[target-nums[i]])