class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 = str(num1)
        num2 = str(num2)
        num3 = str(num3)
        N = max(len(num1), len(num2), len(num3))
        num1 = "0"*(N-len(num1)) + num1
        num2 = "0"*(N-len(num2)) + num2
        num3 = "0"*(N-len(num3)) + num3
        result = ""
        for i in range(N): 
            result += min(num1[i], num2[i], num3[i])
        
        return int(result)
            
