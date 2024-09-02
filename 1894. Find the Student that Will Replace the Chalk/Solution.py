class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        MAXUSE = sum(chalk)
        k %= MAXUSE
        for i in range(len(chalk)): 
            if chalk[i] > k: 
                return i 
            k -= chalk[i]
        return 0
