class MyHashMap:

    def __init__(self):
        self.arr = [None]*1000001

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

    def get(self, key: int) -> int:
        return self.arr[key] if self.arr[key] is not None else -1

    def remove(self, key: int) -> None:
        self.arr[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)