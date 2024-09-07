class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def check(ptr): 
            if len(s)%ptr != 0:
                return False
            for i in range(ptr, len(s), ptr): 
                if s[:ptr] != s[i:i+ptr]:
                    return False
            return True
            
        for i in range(1, len(s)//2+1): 
            if s[i] == s[0] and check(i):
                return True
        
        return False
