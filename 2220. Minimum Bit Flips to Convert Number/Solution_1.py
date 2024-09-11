class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start > goal: 
            start, goal = goal, start
        count = 0
        while goal:
            if (goal & 1) != (start & 1):
                count += 1
            goal >>= 1
            start >>= 1
        
        return count
