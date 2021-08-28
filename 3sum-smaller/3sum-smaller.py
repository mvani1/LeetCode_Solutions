class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        sums = 0
        for i in range(len(nums)-2):
            sums += self.twoSumSmaller(nums,i+1,target-nums[i])
        return sums
    
    def twoSumSmaller(self,nums,start_idx,target):
        sums = 0
        left = start_idx
        right = len(nums)-1
        while left < right:
            if nums[left]+nums[right] < target:
                sums += right - left
                left+=1
            else:
                right -= 1
        return sums