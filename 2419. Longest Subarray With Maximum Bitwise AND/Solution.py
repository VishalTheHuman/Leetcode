class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = 1
        maxVal = -1
        i = 0 
        while i < len(nums): 
            if nums[i] >= maxVal:
                currLength = 1
                val = nums[i]
                i += 1
                while i < len(nums) and nums[i] == nums[i-1]:
                    currLength += 1
                    i += 1
                if val == maxVal:
                    length = max(currLength, length)
                else:
                    length = currLength
                    maxVal = val
            else:
                i += 1
        return length
