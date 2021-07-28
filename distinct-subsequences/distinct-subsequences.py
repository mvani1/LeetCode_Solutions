class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.ans = 0
        self.memo = {}
        self.nd(0,s,t,0)
        return(self.ans)
    def nd(self,start,s,t,i):
        M, N = len(s), len(t)
        if i == M or start == N or M - i < N - start:
            return int(start == len(t))
        
        if (i,start) in self.memo:
            return self.memo[(i,start)]
        
        self.ans = self.nd(start,s,t,i+1)
        
        if t[start] == s[i]:
            self.ans += self.nd(start+1,s,t,i+1)
        self.memo[(i,start)] = self.ans
        return self.ans
            