class Solution:
    def findContestMatch(self, n: int) -> str:
        return self.helper(list(map(str,range(1,n+1))))
    def helper(self,teams):
        if 1 == len(teams):
            return teams[0]
        
        res = []
        
        for i in range(len(teams)//2):
            res.append("("+teams[i]+","+teams[len(teams)-i-1]+")")
        
        return self.helper(res)
    