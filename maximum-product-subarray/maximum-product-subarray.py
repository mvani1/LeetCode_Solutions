class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minn = maxx =result=  nums[0]
        
        
        for i in range(1,len(nums)):
            curr = nums[i]
            temp =(curr,minn*curr,maxx*curr)
            maxx = max(temp)
            minn = min(temp)
            result = max(result,maxx)
        return result
    