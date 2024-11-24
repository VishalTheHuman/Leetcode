class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        nums.insert(0,0)
        answer = float("inf")
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        for i in range(l,r+1):
            for j in range(i,len(nums)):
                val = nums[j] - nums[j-i]
                if val > 0:
                    answer = min(answer, val)
        return answer if answer < float("inf") else -1
