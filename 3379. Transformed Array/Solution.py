class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = nums.copy()
        n = len(nums)
        for i, x in enumerate(nums): 
            if x == 0: 
                result[i] = x
            elif x > 0: 
                idx = (i + x) % n
                result[i] = nums[idx]
            else: 
                idx = (i - (abs(x) % n) + n) % n
                result[i] = nums[idx]
        return result
