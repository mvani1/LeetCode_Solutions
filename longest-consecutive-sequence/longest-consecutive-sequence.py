class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        if not nums:
            return 0
        nums.sort()
        hashSet =set(nums)
        count = 0 
        maxx = 0
        for i in range(len(nums)):
            count = 0
            j = nums[i]
            while j in hashSet:
                count+=1
                j+=1
            maxx = max(maxx,count)
        if maxx == 0:
             return 1
        return(maxx)
            