class Solution:
    def minOperations(self, s: str) -> int:
        store = list(sorted(set(s)))

        if store[0] == 'a': 
            store.pop(0)

        if not store : 
            return 0 

        operations = 0 

        for i in range(1,len(store)):
            operations += (
                ord(store[i]) - ord(store[i-1])
            )
        
        return operations + ord('z') - ord(store[-1]) + 1
