class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:return []
        if len(nums)<2:return [str(nums[0])]
        old = nums[0]
        results = []
        for i in range(1,len(nums)):
            if nums[i]-1 != nums[i-1]:
                new = nums[i-1]
                results.append([old,new])
                old = nums[i]
            if i+1==len(nums):
                results.append([old,nums[i]])
        output = []
        for j in results:
            if j[0]!=j[1]:
                output.append((str(j[0])+"->"+str(j[1])))
            elif j[0]==j[1]:
                output.append(str(j[0]))
        return output