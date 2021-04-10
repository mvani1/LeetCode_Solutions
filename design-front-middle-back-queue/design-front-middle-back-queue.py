class FrontMiddleBackQueue:

    def __init__(self):
        self.stack = []
        self.size = 0

    def pushFront(self, val: int) -> None:
        self.stack.insert(0,val)
        self.size+=1

    def pushMiddle(self, val: int) -> None:
        self.stack.insert(self.size//2,val)
        self.size+=1
    def pushBack(self, val: int) -> None:
        self.stack.append(val)
        self.size+=1

    def popFront(self) -> int:
        if self.stack:
            self.size-=1
            return self.stack.pop(0)
        else:
            return -1

    def popMiddle(self) -> int:
        if self.stack:
            self.size-=1
            return self.stack.pop(self.size//2)
        else:
            return -1

    def popBack(self) -> int:
        if self.stack:
            self.size-=1
            return self.stack.pop()
        else:
            return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()