class Solution:
    def findAndReplacePattern(self, words, pattern):
        pattern = self.counter(pattern)
        ls = []
        for word in words:
            if self.counter(word)==pattern:
                ls.append(word)
        return ls
    
    def counter(self,word):
        dt = {}
        for i in range(len(word)):
            dt[word[i]] = dt.get(word[i],[]) + [i]
        return list(dt.values())