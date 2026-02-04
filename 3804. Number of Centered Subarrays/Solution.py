class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        count = 0 
        
        for i in range(len(nums)): 

            temp = defaultdict(int)
            curr = 0 

            for j in range(i,len(nums)): 

                temp[nums[j]] += 1
                curr += nums[j]

                if curr in temp: 
                    count += 1

        return count
