class Solution:
    def integerBreak(self, n: int) -> int:
        if n<4:
            return n-1
        if n%3==0:
            return 3**int(n/3) 
        elif n%3==1:
            return 4 * 3**(int(n/3)-1)
        else:
            return 2 * 3**(int(n/3))