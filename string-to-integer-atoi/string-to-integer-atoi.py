maxx = (2**31)
minn = -(2**31)
        
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        s = s.lstrip()
        if not s:
            return 0
        
        pn = False # postivie 
        res = '' 
        
        
        if s[0] == '-':
            pn = True
        elif s[0] == '+':
            pn = False
        elif not s[0].isdigit():
            return 0
        else:
            res +=s[0]
            
        for i in range(1, len(s)):
            if not s[i].isdigit():
                break
            else:
                res +=s[i]
        if res == "":
            return 0
        
        res_int = 0
        if pn == False:
            res_int = int(res)
        else:
            res_int = -int(res)
            
        if res_int  >= minn and res_int < maxx-1:
            int_res = res_int 
        elif res_int  <= minn:
            int_res = minn
        else:
            int_res = maxx-1
            
                
        return int_res
                
        