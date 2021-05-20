class Solution:
    def minFlips(self, target: str) -> int:
        state = '0'
        count = 0
        for i in target:
            if state!=i:
                state ='1' if state == '0' else '0'
                count+=1
        return count