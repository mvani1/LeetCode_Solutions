class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        self.n = n
        self.backtrack(out,"",0,0,self.n)
        return out
    
    def backtrack(self,out,string,open,close,max):
        if(len(string) == max*2):
            #base case
            out.append(string)
            return
        if open < max:
            self.backtrack(out,string+'(',open+1,close,max)
        if close < open:
            self.backtrack(out,string+')',open,close+1,max)
            