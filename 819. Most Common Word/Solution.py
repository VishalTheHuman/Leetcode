class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        word = ""
        counter = defaultdict(int)
        for x in paragraph:
            if x in " !?',;.":
                word = word.lower()
                if word and word not in banned:
                    counter[word] += 1
                word = ""
            else:
                word += x
        
        if word and word.lower() not in banned:
            counter[word.lower()] += 1

        answer = ""
        maxCount = 0
        for x,y in counter.items():
            if y > maxCount: 
                answer = x
                maxCount = y

        return answer