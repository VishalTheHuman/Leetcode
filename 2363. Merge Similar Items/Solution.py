class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        store = defaultdict(int)
        for x,y in items1:
            store[x] += y
        for x,y in items2:
            store[x] += y
        return sorted(store.items())
