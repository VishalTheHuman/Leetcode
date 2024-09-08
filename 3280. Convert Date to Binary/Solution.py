class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join([x[2:] for x in list(map(bin, map(int, date.split("-"))))])
