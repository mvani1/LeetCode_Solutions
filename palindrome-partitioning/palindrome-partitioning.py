class Solution:
    '''
        a   a   a   b
    a   1   1   1   0
    
    a   0   1   1   0
    
    a   0   0   1   0
    
    b   0   0   0   0    
    '''
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s,[],res)
        return (res)
    def dfs(self,s,path,res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
                
    def isPalindrome(self,string):
        s = 0
        e = len(string)-1
        while s<e:
            if string[s] != string[e]:
                return False
            s+=1
            e-=1
        return True