class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        temp = {}
        for i in range(len(s)):
            if s[i] not in temp and t[i] not in temp.values():
                temp[s[i]] = t[i]
        res = ""
        # print(temp)
        for i in s:
            res += temp.get(i,"0")
        return res==t
            