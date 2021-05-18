class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        
        for i in range(len(nums)-1,1,-1):
            lo = 0
            hi = i-1
            while lo<hi:
                if nums[lo]+nums[hi]>nums[i]:
                    ans += hi-lo
                    hi-=1
                else:
                    lo+=1
        return(ans)