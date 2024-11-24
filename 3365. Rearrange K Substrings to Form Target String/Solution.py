class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        store = defaultdict(int)
        splits = len(s)//k
        
        for i in range(0,len(s)-splits+1,splits):
            store[s[i:i+splits]] += 1

        for i in range(0,len(t)-splits+1,splits):
            temp = t[i:i+splits]
            if temp not in store:
                return False
            store[temp] -= 1
            if store[temp] == 0:
                del store[temp]
        return len(store) == 0
