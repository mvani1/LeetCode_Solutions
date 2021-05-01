class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stack[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        fetched = self.stack.get(key) 
        try:
            maxx = ('',timestamp)
            for i in range(len(fetched)-1,-1,-1):
                if fetched[i][1]<=maxx[1]:
                    maxx = fetched[i]
                    break
            return maxx[0]
        except:
            return ""
                    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)