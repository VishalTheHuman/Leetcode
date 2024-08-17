class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []
        
        if k == 1:
            return nums
        
        idx = []
        possible = True
            
        for i in range(1, k):
            if (nums[i-1] + 1) != nums[i]:
                idx.append(i-1)
                possible = False
            
        result.append(nums[k-1] if possible else -1)
        
        j = 0
        
        for i in range(k, len(nums)):
            while idx and j == idx[0]:
                idx.pop(0)
            
            if (nums[i-1]+1) != nums[i]:
                idx.append(i-1)
            
            if len(idx)>0:
                result.append(-1)
            else:
                result.append(nums[i])
            
            j += 1
            
        return result
