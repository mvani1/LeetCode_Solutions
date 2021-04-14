class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # for i,v in enumerate(nums):
            
        return all(abs(i-x) <= 1 for i,x in enumerate(nums))
                    
