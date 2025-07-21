class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def solve(n) :
            add = 0 
            product = 1
            while n: 
                num = n%10
                add += num
                product *= num 
                n //= 10
            return add, product
        
        add, product = solve(n)
        
        return (n%(add + product) == 0)
