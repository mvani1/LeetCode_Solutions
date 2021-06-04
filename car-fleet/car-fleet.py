class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position,speed))
        stack = []
        for i in range(n-1,-1,-1):
            pos,s = cars[i]
            arrivalTime = self.getFleetSpeed(target,pos,s)
            if not stack or arrivalTime > stack[-1]:
                stack.append(arrivalTime)
                
        return len(stack)
    def getFleetSpeed(self,target,pos,speed):
        return (target-pos)/speed