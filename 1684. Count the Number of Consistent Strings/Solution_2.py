class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        N = len(allowed)
        count = 0 
        for x in words: 
            if set(x).union(allowed) == allowed: 
                count += 1
        return count
