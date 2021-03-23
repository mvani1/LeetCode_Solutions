class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left,right = [0]*len(nums),[0]*len(nums)
        left[0] = right[-1] = 1
        for i in range(1,len(nums)):
            left[i] = nums[i-1]*left[i-1]
        for j in range(len(nums)-2,-1,-1):
            right[j] = nums[j+1]*right[j+1]
        return [left[k]*right[k] for k in range(len(nums))]