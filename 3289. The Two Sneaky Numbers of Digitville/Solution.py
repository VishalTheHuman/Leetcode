class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []
        for x in nums: 
            if x in seen:
                result.append(x)
            seen.add(x)
        return result
