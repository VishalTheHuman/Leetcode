class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k): 
            minVal = float("inf")
            minIdx = None
            for i in range(len(nums)): 
                if nums[i] < minVal: 
                    minVal = nums[i]
                    minIdx = i 
            if minIdx is not None:
                nums[minIdx] *= multiplier
        return nums
