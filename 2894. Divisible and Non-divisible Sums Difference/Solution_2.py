class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s = 0
        for x in range(n+1):
            if x%m!=0:
                s+=x
            else:
                s-=x
        return sum(x for x in range(n+1) if x%m!=0) - sum(x for x in range(n+1) if x%m==0)