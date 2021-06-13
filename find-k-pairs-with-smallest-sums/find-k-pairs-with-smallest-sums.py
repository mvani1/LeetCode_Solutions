class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        visited = set()
        visited.add((0,0))
        heap = [(nums1[0]+nums2[0],(0,0))]
        out = []
        while len(out) !=k and heap :
            currSum,idx = heapq.heappop(heap)
            idx1,idx2 = idx
            out.append([nums1[idx1],nums2[idx2]])
            if len(nums1) > idx1+1 and (idx1+1,idx2) not in visited:
                heapq.heappush(heap,(nums1[idx1+1]+nums2[idx2],(idx1+1,idx2)))
                visited.add((idx1+1,idx2))
            if len(nums2) > idx2+1 and (idx1,idx2+1) not in visited:
                heapq.heappush(heap,(nums1[idx1]+nums2[1+idx2],(idx1,idx2+1)))
                visited.add((idx1,1+idx2))
        return out
            
                
        
        