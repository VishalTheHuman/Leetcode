class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        idx = 0 
        while idx < len(s):
            start = end = idx
            while end < len(s) and s[start] == s[end]:
                end += 1
            if (end-start-1) >= 2:
                result.append([start, end-1])
            idx = end
        return result
