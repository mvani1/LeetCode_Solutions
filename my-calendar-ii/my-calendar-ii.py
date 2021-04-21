class MyCalendarTwo:

    def __init__(self):
        self.stack = []
        self.freq = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.freq:
            if start < j and end > i:
                return False
        for i,j in self.stack:
            if start < j and end > i:
                self.freq.append((max(start, i), min(end, j)))
        self.stack.append((start,end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)