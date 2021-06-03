class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        maxx = float('-inf')
        heap = []
        
        for i in points:
            x,y = i
            
            if len(heap)>=1:
                while len(heap) >0 and abs(x-heap[0][2])>k:
                    heapq.heappop(heap)
                if len(heap) >0:
                    maxx = max(maxx,abs(heap[0][2]-x)+y+(-heap[0][1]))
            heapq.heappush(heap,(x-y,-y,x))
        return maxx