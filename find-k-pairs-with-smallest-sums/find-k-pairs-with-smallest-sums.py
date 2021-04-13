class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(h,[-(i+j),i,j])
            while k+1<=len(h):
                heapq.heappop(h)
        res = []
        for l in h:
            res.append([l[1],l[2]])
        return res