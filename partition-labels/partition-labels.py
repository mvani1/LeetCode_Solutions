class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {v:i for i,v in enumerate(S)}
        idx=anchor=0
        res = []
        end = 0
        while len(S)>idx:
            start = idx
            end = max(end,last[S[idx]]) 
            if idx == end:
                res.append(len(S[anchor:end+1]))
                anchor = end+1
            
            idx +=1
        return res
