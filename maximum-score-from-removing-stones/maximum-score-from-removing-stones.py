class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = []
        for i in [a,b,c]:
            heapq.heappush(heap,-i)
        count = 0
        while len(heap)>=2:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            count+=1
            x,y = x-1,y-1
            if x> 0:
                heapq.heappush(heap,-x)
                
            if y > 0:
                heapq.heappush(heap,-y)
                
        return count