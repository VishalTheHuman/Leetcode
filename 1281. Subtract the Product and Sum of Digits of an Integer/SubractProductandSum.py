class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        product=1
        while n>0 :
            modulo=n%10
            sum+=modulo
            product*=modulo
            n=n//10
        return product - sum;