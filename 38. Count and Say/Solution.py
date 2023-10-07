class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(2,n+1):
            s = self.string(s)
        return s
    
    def string(self,s):
        count = 1
        j = 1
        ch = s[0]
        s1 = ""
        while j < len(s):
            if ch != s[j]:
                s1+= (str(count)+ch)
                ch = s[j]
                count = 1
            else:
                count+=1 
            j+=1
        s1+=(str(count)+ch)
        return s1