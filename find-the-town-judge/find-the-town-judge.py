class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust ==[] and N==1:return N
        h = {}
        for i in trust:
            if i[1] in h:
                h[i[1]].append(i[0])
            else:
                h[i[1]] =[i[0]]
        trust_check = []
        
        for i in (h.values()):
            trust_check.extend(i)
        for i in range(1,1+N):
            if i in h.keys() and len(h[i]) == N-1 and i not in trust_check:
                return i
        return -1
                
                 