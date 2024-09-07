class Solution:
    def secondHighest(self, s: str) -> int:
        store = set()
        for x in s: 
            if "0" <= x <= "9": 
                store.add(x)
        if len(store) < 2:
            return -1
        return int(sorted(list(store), reverse=True)[1])
