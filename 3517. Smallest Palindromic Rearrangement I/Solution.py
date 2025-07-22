class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(list(s))

        answer = ""
        odd = None

        items = sorted(count.items(), key = lambda x : x[0])

        for key, val in items: 
            if val % 2 == 1: 
                odd = key
            answer += key * (val//2)

        return answer + (odd if odd else "") + answer[::-1]
