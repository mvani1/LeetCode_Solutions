class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Time complexity : O(n^2) Two loops of nn are there.

        Space complexity : O(n). dpdp array of size nn is used.
        '''
        
        dp = [0]*len(nums)
        dp[0] =1
        maxx = 1
        for i in range(1,len(nums)):
            maxval = 0
            for j in range(i):
                if nums[i]>nums[j]:
                    maxval = max(maxval,dp[j])
            dp[i] = maxval+1
            maxx = max(maxx,dp[i])
        return maxx
        