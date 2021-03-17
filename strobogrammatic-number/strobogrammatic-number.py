class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        self.h = {1:1,6:9,9:6,8:8}
        result= ""
        for i in num[::-1]:
            result+=str(self.h.get(int(i),0))
        return result == num