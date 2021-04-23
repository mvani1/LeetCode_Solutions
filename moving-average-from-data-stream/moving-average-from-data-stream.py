class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.cap = size
        self.stack = []

    def next(self, val: int) -> float:
        if len(self.stack)>=self.cap:
            self.stack.pop(0)
        self.stack.append(val)
        return sum(self.stack)/len(self.stack)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)