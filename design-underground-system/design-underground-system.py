class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}
        self.data = collections.defaultdict(lambda :[0,0])
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName,t)
    def checkOut(self, id: int, end_station: str, t: int) -> None:
        startStation,startTime = self.check_ins[id]
        self.data[(startStation,end_station)][0] += (t-startTime)
        self.data[(startStation,end_station)][1] += 1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip,time = self.data[(startStation,endStation)]
        return trip/time

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)