class Solution:
    def findComplement(self, num: int) -> int:
        if num <= 1:
            return num^1
        length = math.log(num,2)
        if int(length) == length:
            length += 1
        remove = 2**(math.ceil(length)) - 1
        return num ^ remove
