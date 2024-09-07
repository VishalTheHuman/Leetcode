class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        K = 0 
        for i in range(len(words)): 
            K += len(words[i])
            if K == len(s): 
                return s == "".join(words[:i+1])
            if K > len(s): 
                return False
        return False
