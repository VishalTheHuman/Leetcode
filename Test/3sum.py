from tqdm import tqdm
class Solution:
    def threeSum(self, nums):
        k=len(nums)
        out=[]
        empty=[]
        i=0
        for x in tqdm(range(k)):
            for y in range(k):
                for z in range(k):
                    if nums[x]+nums[y]+nums[z]==0:
                        if x!=y  and x!=z  and y!=z :
                            empty=[nums[x],nums[y],nums[z]]
                            out.insert(i,empty)
                            i+=1
                            
        for x in range(k):
            for y in range(k):
                for z in range(k):
                    if len(out)>0:
                        return out
                    else:
                        return []

print(Solution.threeSum(Solution,[-1,0,1,2,-1,-4]))