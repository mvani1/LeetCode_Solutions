class Solution:
    def minWindow(self, s: str, s2: str) -> str:
        subs = ""
        minWin = len(s)
        i,j = 0,0
        while i<len(s):
            if s[i] == s2[j]:
                j+=1
            if len(s2) == j :
                j-=1
                end = i
                while j>-1:
                    if s[i] == s2[j]:
                        j-=1
                    i-=1
                j+=1
                i+=1
                if (minWin > end-i):
                    minWin = end-i
                    subs = s[i:end+1]
            i+=1
        return subs
                    