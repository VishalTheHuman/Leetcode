class Solution:
    def finalString(self, s: str) -> str:
        string = ""
        for i in range(len(s)):
            if s[i]!='i':
                string+=s[i]
                continue
            string = string[::-1]
        return string