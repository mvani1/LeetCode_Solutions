class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:return
        old = nums[0]
        res = []
        for i in range(len(nums)-1):
            if nums[i]+1!=nums[i+1]:
                if old!=nums[i]:
                    res.append(( str(old) + '->' + str(nums[i]) ))
                else:
                    res.append((str(old)))
                old = nums[i+1]
            
        if old!=nums[-1]:
            res.append(( str(old) + '->' + str(nums[-1]) ))
        else:
            res.append((str(old)))
        
        return(res)