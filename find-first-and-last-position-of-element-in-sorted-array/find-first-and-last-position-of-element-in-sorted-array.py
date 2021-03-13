class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        count = 1
        l,r=-1,-1
        flag = 0
        for i in range(len(nums)):
            if nums[i]==target:
                l=i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                r=i
                break
        return [l,r]