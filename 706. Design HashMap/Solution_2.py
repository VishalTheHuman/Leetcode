class MyHashMap:

    def __init__(self):
        self.h = [[] for _ in range(100)]
    
    def _get_hash(self,val):
        val = str(val)
        k = 0
        for ch in val:
            k+=ord(ch)
        return k % 100
    
    def put(self, key: int, value: int) -> None:
        h = self._get_hash(key)
        i = 0
        met = False
        for x in self.h[h]:
            if x[0]==key:
                self.h[h].pop(i)
                self.h[h].insert(i,(key,value))
                met = True
                break
            i+=1
        if not met:
            self.h[h].append((key,value))
        
    def get(self, key: int) -> int:
        h = self._get_hash(key)
        for x in self.h[h]:
            if x[0]==key:
                return x[1]
        return -1

    def remove(self, key: int) -> None:
        h = self._get_hash(key)
        if self.h[h]:
            i = 0
            for x in self.h[h]:
                if x[0]==key:
                    self.h[h].pop(i)
                    break
                i+=1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)