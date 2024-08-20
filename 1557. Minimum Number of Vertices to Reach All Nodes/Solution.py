class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        parentArray = [False] * n
        for u,v in edges:
            parentArray[v] = True
        
        return [idx for idx, val in enumerate(parentArray) if not val]
