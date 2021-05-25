class Solution:
    def numSplits(self, s: str) -> int:
        p,q,ans = Counter(),Counter(s),0
        
        for i in s[:-1]:
            p[i] +=1
            q[i] -=1
            if q[i] == 0:
                del q[i]
            ans += len(q) == len(p)
        return ans