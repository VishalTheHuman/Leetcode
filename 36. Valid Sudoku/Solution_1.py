class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        s1 = set()
        s2 = set()
        s3 = set()
        for i in range(n): 
            s1.clear()
            s2.clear()
            s3.clear()
            for j in range(n): 
                e1 = board[i][j] 
                e2 = board[j][i]
                e3 = board[(i%3)*3 + (j//3)][(i//3)*3 + (j%3)]

                if e1 in s1 or e2 in s2 or e3 in s3: 
                    return False

                if e1 != ".": 
                    s1.add(e1)
                if e2 != ".": 
                    s2.add(e2)
                if e3 != ".": 
                    s3.add(e3)

        return True
