class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        i = 0
        ls = []
        while i+1<len(text):
            if text[i]== first and text[i+1]==second:
                if i+2<len(text):
                    ls.append(text[i+2])
            i+=1
        return ls
