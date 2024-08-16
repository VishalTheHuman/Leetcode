class Solution:
    def sortVowels(self, s: str) -> str:
        dt = {}
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                dt[i] = s[i]
        s = list(s)
        for val,ind in zip(sorted(dt.values()),dt.keys()):
            s[ind] = val
        return "".join(s)