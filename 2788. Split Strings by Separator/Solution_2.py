class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        words = separator.join(words)
        string = ""
        ls = []
        for i in range(len(words)):
            if words[i]!=separator:
                string+=words[i]
                continue
            if string:
                ls.append(string)
                string = ""
        if string:
            ls.append(string)
        return ls