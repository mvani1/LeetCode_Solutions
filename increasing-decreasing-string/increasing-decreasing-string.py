class Solution:
    def sortString(self, s: str) -> str:
        f = OrderedDict()
        s = "".join(list(sorted(s)))
        for i in s:
            f[i] = f.get(i,0)+1
        res = ""
        while any(f.values()):
            for k,v in f.items():
                if v>0:
                    res+=k
                    f[k] -=1
            
            for j,vv in reversed(f.items()):
                if vv>0:
                    res+=j
                    f[j] -=1
        return (res)                