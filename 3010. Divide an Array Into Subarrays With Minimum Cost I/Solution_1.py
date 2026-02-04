class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        s1 = s2 = 100
        for x in nums[1:]: 
            if x < s2 or x < s1: 
                s2 = min(s1, s2)
                s1 = x
        return nums[0] + s1 + s2
