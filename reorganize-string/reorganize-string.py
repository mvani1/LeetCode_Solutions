class Solution:
    def reorganizeString(self, s: str) -> str:
        mapping = Counter(s)
        res = ''
        heap = [(-value,key) for key,value in mapping.items()]
        heapq.heapify(heap)
        
        def decrement(char):
            mapping[char] -= 1
            if mapping[char] == 0:
                del mapping[char]
            
        while len(heap) > 0:
            
            _,curr = heapq.heappop(heap)
            _,nextt = heapq.heappop(heap) if heap else (0,'')
            if res and res[-1] == curr:
                return ''
            res += curr+nextt
            decrement(curr)
            decrement(nextt)
            # print(mapping[curr],mapping[nextt])
            if mapping[curr]>0:
                heapq.heappush(heap,(-mapping[curr],curr))
            if mapping.get(nextt,0)>0:
                heapq.heappush(heap,(-mapping[nextt],nextt))
                
        return (res)