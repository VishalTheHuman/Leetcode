class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum=0;
        for i in range(len(nums)):
            sum=sum+nums[i];
            nums[i]=sum;
        return nums