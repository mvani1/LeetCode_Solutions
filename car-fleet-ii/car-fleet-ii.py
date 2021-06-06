class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1]*n
        
        # Already considered last element
        stack = [(float('inf'),cars[-1][0],cars[-1][1])]
        
        for i in range(n-2,-1,-1):
            currPos, currSpeed = cars[i]
            
            while stack and (currSpeed <= stack[-1][2] or ((stack[-1][1] - currPos) / (currSpeed - stack[-1][2]) >= stack[-1][0])):
                stack.pop()
            
            if not stack:
                stack.append((float('inf'),cars[i][0],cars[i][1]))
            else:
                currTime = (stack[-1][1] - currPos) / (currSpeed - stack[-1][2]) 
                stack.append((currTime,cars[i][0],cars[i][1]))
                ans[i] = currTime
        return(ans)