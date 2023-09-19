class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ls = set()
        for i in range(len(nums)):
            if nums[i] in ls:
                return nums[i]
            ls.add(nums[i])
        return -1