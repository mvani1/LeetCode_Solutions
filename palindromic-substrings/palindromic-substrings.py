class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        length = len(s)
        for i in range(length+1):
            for j in range(i,length+1):
                temp = s[i:j]
                if temp == temp[::-1] and temp:
                    result+=1
                    
        return result