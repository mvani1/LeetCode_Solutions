class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # return 'abcacb'
        if k == 0 or k == 1:
            return s
        mapp = Counter(s)
        heap = [(-v,i) for i,v in mapp.items()]
        heapq.heapify(heap)
        i = 0
        res = []
        while len(res) < len(s) and heap:
            freq,char = heapq.heappop(heap)
            if res and char in res[-k+1:]:
                return ""
            res.append(char)
            freq +=1
            
            temp = [(freq,char)] if freq!=0 else []
            i = 0
            
            while i < k-1 and heap:
                nf,nc = heapq.heappop(heap)
                if res and nc in res[-k+1:]:
                    return ""
                res.append(nc)
                nf+=1
                temp.append((nf,nc))
                i+=1
            while temp:
                f,c = temp.pop()
                if f!=0:
                    heapq.heappush(heap,(f,c))
        return "".join(res)