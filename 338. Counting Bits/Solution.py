class Solution:
    def countBits(self, n: int) -> List[int]:
        ls = []
        sum1 = 0
        for x in range(n+1):
            sum1 = bin(x).count("1")
            ls.append(sum1)
        return ls