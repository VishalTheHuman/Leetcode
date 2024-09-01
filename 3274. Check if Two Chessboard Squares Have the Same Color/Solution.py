class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1 = ((ord(coordinate1[0]) - ord("a")) + (int(coordinate1[1])-1)) % 2
        c2 = ((ord(coordinate2[0]) - ord("a")) + (int(coordinate2[1])-1)) % 2
        return c1 == c2
