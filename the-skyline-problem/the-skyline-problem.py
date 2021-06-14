class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)
        if n ==0:
            return []
        if n == 1:
            return [[buildings[0][0],buildings[0][2]],[buildings[0][1],0]]
        
        points = []
        for left,right,height in buildings:
            points.append([left, height, 'start'])
            points.append([right, -height, 'end'])
        points.sort(key=lambda x:( x[0], -x[1]))
        print(points)
        heap = [0]
        output = []
        for point in points:
            if point[2] == 'start':
                if point[1] > -heap[0]:
                    output.append([point[0],point[1]])
                heapq.heappush(heap,-point[1])
            elif point[2] == 'end':
                heap.remove(point[1])
                heapq.heapify(heap)
                if -point[1] > -heap[0]:
                    output.append([point[0],-heap[0]])
        return output
        
#         arr = [0 for _ in range(buildings[-1][1]+1)]
        
#         for xs,xe,h in buildings:
#             for i in range(xs,xe):
#                 arr[i] = max(arr[i],h)
#         stack = []
#         for i,v in enumerate(arr):
#             if v != 0:
#                 stack.append([i,v])
#                 break
        
#         for i in range(stack[-1][0],len(arr)):
#             idx , val = i, arr[i]
#             if val != -1 and stack[-1][1] != val:
#                 stack.append([idx,val])
        
#         return (stack)
        
#         # print(arr)
#         # print(list(range(0,25)))