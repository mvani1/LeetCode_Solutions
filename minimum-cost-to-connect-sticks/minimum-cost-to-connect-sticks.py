class Solution:
    def connectSticks(self, heap: List[int]) -> int:
        heapq.heapify(heap)
        res = []
        while len(heap) != 1:
            f,s = heapq.heappop(heap),heapq.heappop(heap)
            res.append(f+s)
            heapq.heappush(heap,res[-1])
        return sum(res)
            
            