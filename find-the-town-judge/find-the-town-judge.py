class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust ==[] and N==1:return N
        
        h = {}
        out = {}
        for i in trust:
            if i[1] in h:
                h[i[1]].append(i[0])
            else:
                h[i[1]] = [i[0]]
        for i in trust:
            if i[0] in out:
                
                out[i[0]].append(i[1])
            else:
                out[i[0]] = [i[1]]
        for i,vv in h.items():
            if len(h[i]) == N-1 and i not in out:
                    return i
        return -1
        