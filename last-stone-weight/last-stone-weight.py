class Solution:
    def lastStoneWeight(self, heap: List[int]) -> int:
        
        for i in range(len(heap)):
            heap[i] *= -1

        # Heapify all the stones.
        heapq.heapify(heap)
        while len(heap)>=2:
            stone1,stone2 = (heapq.heappop(heap)) , (heapq.heappop(heap))
            if stone1!=stone2:
                new_stone = stone1-stone2
                heapq.heappush(heap,new_stone)
        return -1*heapq.heappop(heap) if heap else 0 
        