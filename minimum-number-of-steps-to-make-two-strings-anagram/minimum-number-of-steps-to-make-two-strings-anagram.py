class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if len(s)!= len(t):
            return 0
        ss = collections.Counter(s)
        c=0
        for i in t:
            ss[i] = ss.get(i,0)-1
            if ss[i]<0:
                c+=1
        return c