class Solution:
    def firstUniqChar(self, s: str) -> int:
        fre_counter = {}
        result = 0
        for i in s:
            fre_counter[i] = fre_counter.get(i,0)+1
        for j,v in fre_counter.items():
            if v==1:
                return s.index(j)
        return -1