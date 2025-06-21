class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <= k and m <= k: 
            return 0 
        cost = 0
        if n > k:
            cost += (n-k) * k        
        if m > k:
            cost += (m-k) * k
        return cost
