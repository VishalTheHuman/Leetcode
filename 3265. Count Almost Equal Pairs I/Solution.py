class Solution:
    def countPairs(self, nums: List[int]) -> int:
        count = 0 
        
        for i in range(len(nums)): 
            nums[i] = str(nums[i])
        
        store1 = defaultdict(int)
        store2 = defaultdict(int)
        
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)): 
                if nums[i] == nums[j]:
                    count += 1
                    continue
                    
                temp = 0
                length = max(len(nums[i]), len(nums[j]))
                x = nums[i].zfill(length)
                y = nums[j].zfill(length)
                
                    
                for idx in range(length): 
                    if x[idx]!=y[idx]: 
                        temp += 1
                    store1[x[idx]]+=1
                    store2[y[idx]]+=1
                    
                possible = True
                for x in store1:
                    if store1[x]!=store2[x]:
                        possible = False
                        break
                    
                if possible and (temp == 2): 
                    count +=1
                
                store1.clear()
                store2.clear()
        return count
