class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)-1):            
                if nums[i]<nums[j]<max(nums[j+1:]):
                    return True
        return False