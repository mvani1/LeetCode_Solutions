class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        indexes_removed = []
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] ==y:
                indexes_removed.append(points[i]) 
        if not indexes_removed:return -1
        h = OrderedDict()
        minn = (math.inf,0)
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] ==y:
                h[i] = abs(x-points[i][0])+abs(y-points[i][1])
                if h[i]<minn[0]:
                    minn=(h[i],i)
        print(h)
        return minn[1]
