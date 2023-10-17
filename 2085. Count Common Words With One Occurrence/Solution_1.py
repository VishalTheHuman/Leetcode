class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1 = Counter(words1)
        words2 = Counter(words2)
        count = 0
        for key,val in words1.items():
            if val == words2.get(key,0) == 1:
                count +=1
        return count 
