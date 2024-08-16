class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for x in nums:
            for y in nums:
                if y==original:
                    original=2*original
        return original