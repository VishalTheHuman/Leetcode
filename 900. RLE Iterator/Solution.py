class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.ptr = 0
        self.N = len(encoding)

    def next(self, n: int) -> int:
        if self.ptr >= self.N: 
            return -1
        answer = -1
        while n and self.ptr < self.N: 
            while self.ptr < self.N and self.encoding[self.ptr] == 0:
                self.ptr += 2
            if self.ptr < self.N:
                toRemove = min(n, self.encoding[self.ptr])
                n -= toRemove
                self.encoding[self.ptr] -= toRemove
                answer = self.encoding[self.ptr+1]
        return answer if n==0 else -1
                

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
