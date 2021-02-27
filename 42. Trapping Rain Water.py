class Solution:
    def trap(self, height: List[int]) -> int:
        result = []
        for i in range(len(height)):
            left = max(height[:i+1])
            right = max(height[i:])
            result.append(min(left,right)-height[i])
        return sum(result)