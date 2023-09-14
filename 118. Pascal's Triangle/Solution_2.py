class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ls = [[1]*x for x in range(1,numRows+1)]
        if numRows <=2: return ls
        for x in range(1,numRows):
            for y in range(1,x):
                ls[x][y] = ls[x-1][y]+ls[x-1][y-1]
        return ls