class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        s1 = set()
        s2 = set()
        for i in range(n): 
            s1.clear()
            s2.clear()
            for j in range(n): 
                if board[i][j] in s1: 
                    return False
                if board[j][i] in s2: 
                    return False
                if board[i][j] != ".": 
                    s1.add(board[i][j])
                if board[j][i] != ".": 
                    s2.add(board[j][i])

            for x in range(3): 
                for y in range(3): 
                    s1.clear()
                    for i in range(3): 
                        for j in range(3):
                            if board[x*3 + i][y*3 + j] in s1: 
                                return False

                            if board[x*3 + i][y*3 + j]!= ".": 
                                s1.add(board[x*3 + i][y*3 + j])

        return True
