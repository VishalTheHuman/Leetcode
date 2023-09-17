class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        rt = []
        for i in range(len(nums)):
            n = [nums[i]]
            test = nums[:i]+nums[i+1:]
            for x in self.permute(test):
                rt.append(n+x)
        return rt