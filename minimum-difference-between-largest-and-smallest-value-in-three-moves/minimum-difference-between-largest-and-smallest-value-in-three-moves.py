class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        
        maxV, minV = [-float('inf')] * 4, [float('inf')] * 4
        for n in nums:
            if n > maxV[0]:
                maxV[0] = n
                for i in range(0, 3):
                    if maxV[i] > maxV[i + 1]:
                        maxV[i], maxV[i + 1] = maxV[i + 1], maxV[i]     
            if n < minV[0]:
                minV[0] = n
                for i in range(0, 3):
                    if minV[i] < minV[i + 1]:
                        minV[i], minV[i + 1] = minV[i + 1], minV[i]
        
        return min(maxV[i] - minV[3 - i] for i in range(4)) 