class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        q = deque()
        for i in range(k - 1):
            while len(q) and (q[-1] < nums[i]):
                q.pop()
            q.append(nums[i])
        
        out = []
        for i in range(k - 1, len(nums)):
            while len(q) and (q[-1] < nums[i]):
                q.pop()
            q.append(nums[i])
            out.append(q[0])
            if (q[0] == nums[i - k + 1]):
                q.popleft()
        
        return out