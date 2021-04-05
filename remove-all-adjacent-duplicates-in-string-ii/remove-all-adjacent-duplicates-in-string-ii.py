class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count = 0
        i=0
        temp = s
        for j in range(len(set(s))):
            for i in set(s):
                temp = temp.replace(k*i,"")
        
        return (temp)