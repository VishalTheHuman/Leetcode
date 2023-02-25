class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum=0
        count=0
        for x in nums:
            if (x%2==0) and (x%3==0):
                sum+=x
                count=count+1
        if count == 0:
            return 0
        return sum//count
