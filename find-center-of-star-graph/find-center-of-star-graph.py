class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        lists = range(1,len(edges)+2)
        h = {x:[] for x in range(1,len(edges)+2)}
        
        for i in edges:
            # print(i[0],i[1])
            h[i[0]].append(i[1])
            h[i[1]].append(i[0])
        for i in h:
            if len(h[i]) == len(h.keys())-1:
            
                return i
            