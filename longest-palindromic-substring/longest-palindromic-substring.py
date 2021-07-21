class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) < 1:
            return ""
        start,end = 0,0
        for i in range(len(s)):
            length = max(self.ee(s,i,i),self.ee(s,i,i+1))
            if length > end - start:
                start = i-(length-1)//2
                end = i +length//2
        return s[start:end+1]
    def ee(self,s,left,right):
        L = left
        R = right
        while(L>=0 and R< len(s) and s[L] == s[R]):
            L-=1
            R+=1
        return R - L - 1