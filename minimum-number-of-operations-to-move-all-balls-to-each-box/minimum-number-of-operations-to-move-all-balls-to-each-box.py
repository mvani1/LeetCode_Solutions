class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left,right,lc,rc = [0 for _ in range(n)],[0 for _ in range(n)],[0 for _ in range(n)],[0 for _ in range(n)]
        
        for i in range(1,n):
            left[i] = int(boxes[i-1])+left[i-1]
            lc[i] = left[i]+lc[i-1]
            
        for i in range(n-2,-1,-1):
            right[i] = int(boxes[i+1])+right[i+1]
            rc[i] = right[i]+rc[i+1]
            
        return list(map(lambda x,y:x+y,lc,rc))        