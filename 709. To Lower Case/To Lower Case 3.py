class Solution:
    def toLowerCase(self, s: str) -> str:
        k = list(s)
        out =""
        for x in range(len(k)):
            if ord(k[x])>=65 and ord(k[x])<=90:
                out+=chr(ord(k[x])+32)
            else:
                out+=k[x]
        return out