class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums)/3 
        ans = Counter(nums)
        return [x for x in ans if ans[x]>l]