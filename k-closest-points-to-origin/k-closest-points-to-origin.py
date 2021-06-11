class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        getDistance = lambda x,y: (x**2+y**2)
        # getSquareRoot = lambda x: math.sqrt(x)     
        for i in points:
            distance = getDistance(i[0],i[1])
            # result = getSquareRoot(distance)
            heapq.heappush(heap,((distance,i)))
        ans = []
        while heap and k!=0:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans
        # return [(heap[:k])]