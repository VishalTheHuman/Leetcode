class Solution:
    def checkRecord(self, s: str) -> bool:
        l = a = 0
        for x in s: 
            if x == "L": 
                l += 1
                if l==3:
                    return False
            else:
                if l:
                    l = 0
                if x == "A":
                    a += 1
                    if a >= 2: 
                        return False
        
        return True
