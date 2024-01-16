from random import choice
class RandomizedSet:

    def __init__(self):
        self.ls = {}

    def insert(self, val: int) -> bool:
        if val not in self.ls:
            self.ls[val] = val
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.ls:
            return False
        del self.ls[val]
        return True

    def getRandom(self) -> int:
        return choice(list(self.ls.keys()))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
