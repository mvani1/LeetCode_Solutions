class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = max_sum = minn = nums[0]
        for i in range(1,len(nums)):
            maxx = max(maxx+nums[i],nums[i])
            max_sum = max(max_sum,maxx)
        return max_sum
