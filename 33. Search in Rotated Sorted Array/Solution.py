class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        mid = len(nums)//2
        while l < r and nums[mid] != target: 
            if nums[mid] > target: 
                if nums[l] > nums[mid] or nums[l] <= target: 
                    r = mid - 1
                else: 
                    l = mid + 1
            else: 
                if nums[r] < nums[mid] or nums[r] >= target: 
                    l = mid + 1
                else: 
                    r = mid -1 
            mid = (l+r)//2
        return mid if nums[mid] == target else -1
