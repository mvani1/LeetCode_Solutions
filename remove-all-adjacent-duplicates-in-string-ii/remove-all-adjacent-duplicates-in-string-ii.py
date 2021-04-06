class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ss = set(s)
        c=10
        for p in range(len(ss)):
            if len(s)<k:
                break
            for i in ss:
                s = s.replace(i*k,"")
            # print(s,len(s))
            c-=1
        return(s)