class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        diff = mean * (m+n) - sum(rolls)
        if (diff/n) > 6 or diff < n: 
            return []
        remain = diff % n 
        result = [diff//n + (1 if (remain - i) > 0 else 0) for i in range(n)]
        return result
