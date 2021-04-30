class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        heapq.heappush(heap, intervals[0][1])
        for s,e in intervals[1:]:
            
            if heap and heap[0]<=s:
                heapq.heappop(heap)
            heapq.heappush(heap,e)
            
        return len(heap)