class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        if len(s)==1 or s==s[::-1]:
            return s
        result = []
        for i in range(len(s)-1,-1,-1):
            temp = (s[i:][::-1]+s)
            if temp == temp[::-1]:
                return temp