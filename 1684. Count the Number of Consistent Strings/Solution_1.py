class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        N = len(allowed)
        count = 0 
        for x in words: 
            for y in x: 
                if y not in allowed:
                    count += 1
                    break
    
        return len(words) - count
