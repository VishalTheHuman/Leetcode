class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        diff = mean * (m+n) - sum(rolls)
        if (diff/n) > 6 or diff < n: 
            return []
        result = [diff//n]*(n)
        remain = diff % n 
        i = 0
        while remain>0:
            toAdd = min(6 - result[i], remain)
            result[i] += toAdd
            remain -= toAdd
            i += 1
        return result
