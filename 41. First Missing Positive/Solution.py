class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dt = Counter(nums)
        i = 1
        while True:
            if not dt.get(i,False):
                return i
            i+=1
