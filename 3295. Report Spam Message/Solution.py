class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        message = Counter(message)
        bannedWords = set(bannedWords)
        count = 0 
        for x in bannedWords:
            if x not in message:
                continue
            count += message[x]
            if count >= 2:
                return True
        return False
