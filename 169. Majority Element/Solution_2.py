class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = Counter(nums)
        max_val = 0
        max_ = 0
        for x in ans:
            if ans[x] > max_:
                max_ = ans[x]
                max_val = x
        return max_val