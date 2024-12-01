class Solution:
    def smallestNumber(self, n: int) -> int:
        return 2**(len(bin(n)[2:]))-1
