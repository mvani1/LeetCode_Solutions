class LogSystem:

    def __init__(self):
        self.stack = []
        self.compare = {'Year':4,'Month':7,'Day':10,'Hour':13,'Minute':16,'Second':19}

    def put(self, id: int, timestamp: str) -> None:
        self.stack.append((id,timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        limit = self.compare[granularity]
        start_limit = start[:limit]
        end_limit = end[:limit]
        for i,v in self.stack:
            if v[:limit]>=start_limit and end_limit>=v[:limit]:
                yield i
                


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)