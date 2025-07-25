class Solution:
    def maxSum(self, nums: List[int]) -> int:
        answer = 0 
        seen = set()
        minimumNegative = -1000
        for x in nums: 
            if x < 0: 
                minimumNegative = max(minimumNegative, x)
            elif x not in seen: 
                answer += x
                seen.add(x)
        
        if answer > 0: 
            return answer
        elif 0 in seen: 
            return 0 
        else:
            return minimumNegative
