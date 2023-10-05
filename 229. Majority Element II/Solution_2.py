class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums)//3 
        dt = {}
        ls = []
        for x in nums:
            val = dt.get(x,0)
            dt[x] = val + 1
            if dt[x] > l and x not in ls:
                ls.append(x) 
        return ls