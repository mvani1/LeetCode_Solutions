class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = minn =result = nums[0]
        for i in range(1,len(nums)):
            curr = nums[i]
            temp = (curr,curr*minn,curr*max_so_far)
            minn = min(temp)
            max_so_far = max(temp)
            result = max(max_so_far,result)
        return result