class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        word = ""
        words = []
        for x in text:
            if x == " ":
                spaces += 1
                if word:
                    words.append(word)
                    word = ""
            else:
                word += x
        if word:
            words.append(word)
        if (len(words)-1) > 0:
            extra = spaces % (len(words)-1)
            return (" "*(spaces//(len(words)-1))).join(words) + " "*extra
        return "".join(words) + " "*spaces
