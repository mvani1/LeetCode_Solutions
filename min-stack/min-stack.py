class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or val<=self.getMin():
            self.min.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped== self.getMin():
            self.min.pop()
        return popped

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()