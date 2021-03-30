class MyCalendar:

    def __init__(self):
        self.list = []

    def book(self, start: int, end: int) -> bool:
        flag = 0
        if self.list:
            for s,e in self.list:
                if s<end and start<e:return False
        self.list.append((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)