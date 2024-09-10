class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def findRook():
            for i in range(8): 
                for j in range(8): 
                    if board[i][j] == "R": 
                        return i, j
        
        def solve(i, j, itr, isRow):
            for idx in itr:
                if (board[idx][j] if isRow else board[i][idx]) == "B":
                    break
                elif (board[idx][j] if isRow else board[i][idx]) == "p":
                    return 1
            return 0
        
        i, j = findRook()
        count = 0 
        iters = [
            (range(i-1,-1, -1), True), 
            (range(i+1,8), True), 
            (range(j-1, -1, -1), False), 
            (range(j+1, 8), False)
        ]

        for itr, isRow in iters:
            count += solve(i,j, itr, isRow)
        return count
