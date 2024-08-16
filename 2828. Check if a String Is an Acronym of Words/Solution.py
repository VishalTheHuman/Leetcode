class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        string = ""
        for x in words:
            string+=x[0]
        return string==s