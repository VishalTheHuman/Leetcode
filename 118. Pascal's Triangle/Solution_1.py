class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ls = [[1]]
        for x in range(2,numRows+1):
            a = [1,1]
            i = 0
            j = 1
            while len(a)<x:
                a.insert(1,ls[-1][i]+ls[-1][j])
                i+=1
                j+=1  
            ls.append(a)
        return ls