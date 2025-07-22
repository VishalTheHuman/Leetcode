class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        last_seen = {}
        subarraySum = currSum = left = 0
        for idx, val in enumerate(nums): 
            currSum += val 
            if val in last_seen: 
                while left <= last_seen[val]: 
                    currSum -= nums[left]
                    left += 1
            last_seen[val] = idx
            subarraySum = max(subarraySum, currSum) 
        return subarraySum
