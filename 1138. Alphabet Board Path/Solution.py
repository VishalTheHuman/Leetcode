class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        mapping = {chr(ord("a")+i) : (i//5, i%5) for i in range(26)}
        X = Y = 0
        result = ""
        for ch in target: 
            newX, newY = mapping[ch]
            if ch == "z": 
                result += ("L"*(Y-newY) + "D"*(newX-X))
            else:
                result += ("D" if newX > X else "U")*abs(newX-X) + ("R" if newY > Y else "L")*abs(newY-Y)
            result += "!"
            X,Y = newX, newY
        return result
