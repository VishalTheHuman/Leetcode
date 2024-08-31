class Solution:
    def stringHash(self, s: str, k: int) -> str:
        mapping = {chr(ord("a")+i) : i for i in range(26)}
        result = ""
        for i in range(0,len(s), k): 
            curr = 0
            for x in s[i:i+k]:
                curr += mapping[x]
            curr %= 26
            result += chr(ord("a")+curr)
        return result
