maxx = (2**31)
minn = -(2**31)-1
        
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s or s[0].isalpha():
            return 0
        r = ""
        flag = 0
        for i in s:
            if i.isdigit():
                flag = 1
            if flag and not i.isdigit(): #in ['-','+','1','2','3','4','5','0','6','7','8','9']:
                break
            r += i
        if '+' in r and '-' in r:
            return 0
        if ' ' in r and '-' in r:
            return 0
        if '+' in r and ' ' in r:
            return 0
        
        try:    
            if int(r)>=maxx:return maxx-1 
            if int(r)<=minn: return minn+1
        except:
            return 0
        return int(r)
                
            
            
                
        