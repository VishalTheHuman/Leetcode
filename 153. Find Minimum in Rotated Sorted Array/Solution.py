class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        mid = (l+r)//2
        while l < r: 
            if nums[mid] > nums[r]: 
                l = mid + 1
            else: 
                r = mid 
            mid = (l+r)//2
        return nums[mid]
