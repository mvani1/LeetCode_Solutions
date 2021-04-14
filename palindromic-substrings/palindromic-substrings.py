class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        left, right = 0,len(s)
        for i in range(len(s)):
            right = len(s)
            while left<=right:
                pal = (s[left:right])
                
                if pal and pal == pal[::-1]:
                    res+=1
                right-=1
            left+=1
        return res