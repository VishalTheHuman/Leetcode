class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n): 
            num = 0
            while n:
                num = num*10 + n%10
                n//=10
            
            return num 
        
        return abs(n - reverse(n))
