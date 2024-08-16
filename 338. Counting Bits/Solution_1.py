class Solution:
    def countBits(self, n: int) -> List[int]:
        ls = [0] * (n+1)
        for x in range(1,n+1):
            ls[x] = ls[x//2] + x%2
        return ls