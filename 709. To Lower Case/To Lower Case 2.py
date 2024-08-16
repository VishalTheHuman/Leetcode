class Solution:
    def toLowerCase(self, s: str) -> str:
        out =""
        for x in range(len(s)):
            if ord(s[x])>=65 and ord(s[x])<=90:
                out+=chr(ord(s[x])+32)
            else:
                out+=s[x]
        return out