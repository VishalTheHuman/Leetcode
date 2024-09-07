class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        store = set()
        num = ""
        numFound = False
        for x in word: 
            if x in "qwertyuiopasdfghjklzxcvbnm": 
                if num or numFound: 
                    if num:
                        store.add(num)
                    elif numFound:
                        store.add("0")
                    num = ""
                    numFound = False
                continue

            numFound = True
            if x == "0" and num:
                num += x
            if x != "0": 
                num += x
        if num:
            store.add(num)
        elif numFound:
            store.add("0")

        return len(store)
