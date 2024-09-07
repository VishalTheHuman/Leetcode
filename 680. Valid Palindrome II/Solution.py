class Solution:
    def validPalindrome(self, s: str) -> bool:
        def find(l, r, possible = True): 
            while l <= r: 
                if s[l]!=s[r]:
                    if possible:
                        return find(l+1, r, False) or find(l, r-1, False)
                    return False
                l += 1
                r -= 1
            return True
        return find(0,len(s)-1)
