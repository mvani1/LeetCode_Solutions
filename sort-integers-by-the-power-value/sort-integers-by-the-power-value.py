class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        odd = lambda x:3*x+1
        even = lambda x:x//2
        res = []
        for i in range(lo,hi+1):
            count = [0,i] 
            while i!=1:
                if i&1:
                    i=odd(i)
                    count[0]+=1
                else:
                    i= even(i)
                    count[0]+=1
            res.append(count)
        res.sort(key = lambda x:(x[0],x[1]))
        out =[]
        for i in res:
            out.append(i[1])
        return out[k-1]