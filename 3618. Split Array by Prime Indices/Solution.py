class Solution:
    def splitArray(self, nums: List[int]) -> int:
        length = len(nums)
        i = 2
        indicesToRemove = set([0,1])
        for i in range(2, (length//2 + 1)): 
            for j in range(2,(length//2 + 1)): 
                if i*j > length: 
                    break
                indicesToRemove.add(i*j)

        a = b = 0 
        for idx, x in enumerate(nums): 
            if idx in indicesToRemove: 
                b += x
            else: 
                a += x

        return abs(a-b)
