class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def addNum(self, num: int) -> None:
        self.s.append(num)

    def findMedian(self) -> float:
        self.s.sort()
        if len(self.s)&1: # odd
            return self.s[len(self.s)//2]
        else:
            return (self.s[(len(self.s)//2)-1]+self.s[len(self.s)//2])/2
        # return 1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()