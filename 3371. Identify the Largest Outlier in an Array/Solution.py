class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        store = defaultdict(int)
        for x in nums: 
            store[x] += 1
            
        outlier = float("-inf")
        total = sum(nums)
        
        for x in nums: 
            curr = total - x
            
            if store[x] == 1:
                del store[x]
            else:
                store[x] -= 1
                
            if (curr/2) in store: 
                outlier = max(outlier, x)

            store[x] += 1
        return outlier
