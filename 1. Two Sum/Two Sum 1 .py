class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k=len(nums)
        for x in range(k):
            for y in range(k):
                if nums[x]+nums[y]==target and x!=y:
                    return [x,y]
        return []        