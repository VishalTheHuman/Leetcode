class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n <= 1:
            return n^1
        length = math.log(n,2)
        if int(length) == length:
            length += 1
        remove = 2**(math.ceil(length)) - 1
        return n ^ remove
