class Solution:
    def decodeString(self, s: str) -> str:
        digits = re.findall('\d*',s)
        digits = list(filter(None, digits))
        for i in range(len(s)-1,-1,-1):
            if s[i] in ['0','1','2','3','4','5','6','7','8','9']:
                j=i+2
                res = ''
                while j<len(s) and s[j]!=']':
                    res+=s[j]
                    j+=1
                ss = digits.pop()
                
                new_res = (int(ss)*res)
                s = s.replace(ss+s[i+1:j+1],new_res)
        return (s)
            