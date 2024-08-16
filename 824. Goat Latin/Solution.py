class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split(" ")
        count=1
        for idx in range(len(sentence)):
            if sentence[idx][0] in "aeiouAEIOU":
                sentence[idx] = sentence[idx]+"ma"+ "a"*count
            else:
                sentence[idx] = sentence[idx][1:]+sentence[idx][0]+"ma"+"a"*count
            count+=1
        return " ".join(sentence)