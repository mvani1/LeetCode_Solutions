class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            if k > len(heap):
                heapq.heappush(heap, i)
            else:
                heapq.heappushpop(heap,i)
        return heap[0]