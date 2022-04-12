class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + [0]*n
        for i in nums:
            nums[i+n] = nums[nums[i]]
        nums = nums[n:]
        return(nums)