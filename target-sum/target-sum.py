class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.counter = 0 
        self.hash = {}
        self.start_find_ways(nums,0,0,target)
        return self.hash[(0,0)]
    
    def start_find_ways(self,nums,start,sums,target):
        if (start,sums) in self.hash:
            return self.hash[(start,sums)]
        
        if start == len(nums):
            if sums == target:
                return 1
            else:
                return 0 
        else:
            ans = self.start_find_ways(nums,start+1,sums+nums[start],target)\
            + self.start_find_ways(nums,start+1,sums-nums[start],target)
        self.hash[(start,sums)] = ans
        return ans

            
