class Solution:
    def freqAlphabets(self, s: str) -> str:
        string = ""
        i = len(s)-1
        while i>=0:
            if s[i]=="#":
                string+=chr(int(s[i-2:i]) + ord('a')-1)
                i-=3
                if i<0: break
                continue
            string+= chr(int(s[i])+ord('a')-1)
            i-=1
        return string[::-1]