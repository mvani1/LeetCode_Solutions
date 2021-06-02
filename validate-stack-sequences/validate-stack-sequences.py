class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(popped)
        idx = 0
        s = []
        for i in range(n):
            while s and s[-1] == popped[idx]:
                s.pop()
                idx+=1
            s.append(pushed[i])
        while s and s[-1] == popped[idx]:
            s.pop()
            idx+=1
        return not s