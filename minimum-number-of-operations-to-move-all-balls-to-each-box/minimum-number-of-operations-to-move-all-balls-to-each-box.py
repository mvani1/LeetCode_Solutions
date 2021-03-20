class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left,right = [0]*n,[0]*n
        
        count_1,count_2 = int(boxes[0]),int(boxes[-1])
        
        for i in range(1,len(boxes)):
            left[i] = left[i-1]+count_1
            if boxes[i] == '1':
                count_1+=1
        for i in range(len(boxes)-2,-1,-1):
            right[i] = right[i+1]+count_2
            if boxes[i] == '1':
                count_2+=1
        return list(map(lambda x,y:x+y,left,right))
                
                
                
            