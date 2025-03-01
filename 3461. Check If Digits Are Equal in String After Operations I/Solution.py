class Solution:
    def hasSameDigits(self, s: str) -> bool:
        store = list(map(int, list(s)))
        while len(store) > 2: 
            curr = []
            for i in range(1,len(store)): 
                curr.append((store[i-1] + store[i]) % 10)
            store = curr[:]
        return len(store) ==2 and store[0]==store[1]
