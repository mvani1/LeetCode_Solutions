class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right =0,0
        tt=collections.Counter(t)
        target = 0 
        res = ""
        for i in s:
            if i in t and tt.get(i)>0:
                target+=1
            tt[i] = tt.get(i,0)-1
            
            while target == len(t):
                if res and len(res)>=len(s[left:right+1]):
                    res = s[left:right+1]
                if not res:
                    res = s[left:right+1]
                if s[left] in t and tt.get(s[left])==0:
                    target-=1
                    
                tt[s[left]] = tt.get(s[left],0)+1
                left+=1
            right+=1
        return (res) 