class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Time complexity : O(n^2) Two loops of nn are there.

        Space complexity : O(n). dpdp array of size nn is used.
        '''
        
        dp = [1]*len(nums)
        maxx = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
            maxx = max(maxx,dp[i])
        return max(dp)