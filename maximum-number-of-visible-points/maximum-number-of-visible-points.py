class Solution:
    def visiblePoints(self, points: List[List[int]], givenAngle: int, location: List[int]) -> int:

        angles = []
        duplicate = 0
        
        for point in points:
            if point == location: 
                duplicate+=1
            else:
                angles.append(self.getAngle(point,location))
        
        angles.sort()
        ans = 0
        queue = deque()

        for angle in angles:
            queue.append(angle)
            
            while angle - queue[0] > givenAngle:
                queue.popleft()
                
            ans = max(ans,len(queue))
            
        for angle in angles:
            angle+=360
            queue.append(angle)
            
            while angle - queue[0] > givenAngle:
                queue.popleft()
                
            ans = max(ans,len(queue))
        return ans + duplicate
        
    def getAngle(self,point,location):
        x,y = point
        initial_x,initial_y = location
        angle = math.atan2(x-initial_x,y-initial_y)/(2*math.pi)*360
        return angle+360 if angle<0 else angle