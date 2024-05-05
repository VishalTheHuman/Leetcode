class Solution:
    def minAnagramLength(self, s: str) -> int:
        s = Counter(s)
        gcd_val = None
        def gcd(a,b):
            if a is None:
                return b
            while b:
                a, b = b, a % b
            return a
        
        for x,y in s.items():
            gcd_val = gcd(gcd_val, y)
        
        count = 0 
        for x,y in s.items():
            count += (y//gcd_val)
        
        return count
