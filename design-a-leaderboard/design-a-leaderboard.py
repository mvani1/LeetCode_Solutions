class Leaderboard:

    def __init__(self):
        self.leader = collections.defaultdict(lambda :0)

    def addScore(self, playerId: int, score: int) -> None:
        self.leader[playerId] += score
        

    def top(self, K: int) -> int:
        heap = []
        for v in self.leader.values():
            heapq.heappush(heap,v)
            if len(heap)>K:
                heapq.heappop(heap)
        return sum(heap)

            
    def reset(self, playerId: int) -> None:
        del self.leader[playerId]
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)