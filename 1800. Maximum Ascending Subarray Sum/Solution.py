class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        nums.insert(0,0)
        maxSum = 0
        curr = 0
        for i in range(1,len(nums)): 
            if nums[i] > nums[i-1]:
                curr += nums[i]
            else:
                maxSum = max(maxSum, curr)
                curr = nums[i]
        maxSum = max(maxSum, curr)
        return maxSum
