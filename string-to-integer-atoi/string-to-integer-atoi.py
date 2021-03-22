class Solution:
    def myAtoi(self, s: str) -> int:
        strr = s.strip()
        beg = re.findall("^[\+\-]?\d+", strr)
        minn,maxx = -2**31,2**31-1
        if beg:
            result = int(beg[0])
            if result>minn and result<maxx:
                return result
            elif result<=minn:
                return minn
            elif result>=maxx:
                return maxx
                
        
        return 0