class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ls = []
        for x in words:
            x = x.split(separator)
            ls.extend([i for i in x if i])
        return ls