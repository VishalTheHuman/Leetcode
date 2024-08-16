class MyStack:

    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []

    def push(self, x: int) -> None:
        self.queue_1.append(x)

    def pop(self) -> int:
        while len(self.queue_1)>1:
            self.queue_2.append(self.queue_1.pop(0))
        ret = self.queue_1.pop()
        while len(self.queue_2)>0:
            self.queue_1.append(self.queue_2.pop(0))
        return ret

    def top(self) -> int:
        while len(self.queue_1)>1:
            self.queue_2.append(self.queue_1.pop(0))
        ret = self.queue_1.pop()
        while len(self.queue_2)>0:
            self.queue_1.append(self.queue_2.pop(0))
        self.queue_1.append(ret)
        return ret

    def empty(self) -> bool:
        return len(self.queue_1)==0
    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()