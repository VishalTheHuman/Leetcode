class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return [x[0] for x in words] == list(s)~