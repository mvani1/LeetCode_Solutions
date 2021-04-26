class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sets = set()
        nums.sort()
        for i ,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            
            while left<right:
                sums = nums[i]+nums[left]+nums[right]
                res = [nums[i],nums[left],nums[right]]
                if sums > 0:
                    right-=1
                elif sums < 0:
                    left+=1 
                else:
                    result.append(res)
                    left +=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
                    
        return (result)