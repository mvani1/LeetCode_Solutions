class Solution:
    def shortestSubarray(self, nums: List[int], K: int) -> int:
        P = [0]
        N = len(nums)
        for i in nums:
            P.append(P[-1]+i)
        
        ans = N+1
        mono_q = deque()
        
        for y,Py in enumerate(P):
            while mono_q and Py < P[mono_q[-1]]:  
                mono_q.pop()
            while mono_q and Py - P[mono_q[0]] >= K:
                ans = min(ans,y-mono_q.popleft())
            mono_q.append(y)
        return ans if ans<N+1 else -1
                