class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        ans = [0]*n
        stack = []
        
        for i in range(n-1,-1,-1):
            while stack and T[stack[-1]] <=T[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]-i
            stack.append(i)
        return ans 