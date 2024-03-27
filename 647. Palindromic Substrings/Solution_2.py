class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(1, len(s)+1):
            for j in range(len(s)-i+1):
                k = s[j:j+i]
                if k == k[::-1]:
                    count += 1
        return count 
