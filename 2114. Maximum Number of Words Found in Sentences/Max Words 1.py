class Solution:
    def mostWordsFound(self, sentences) -> int:
        maxcount=1
        count=1
        for x in sentences:
            for y in x:
                if y == " ":
                    count+=1
            if count>maxcount:
                maxcount=count
            count=1
        return maxcount