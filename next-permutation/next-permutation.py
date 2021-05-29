class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        decEle = len(nums)-2
        while decEle>=0 and nums[decEle+1]<= nums[decEle]:
            decEle-=1
        
        if decEle >=0:
            justGreater = len(nums)-1
            while nums[justGreater]<=nums[decEle]:
                justGreater-=1
            
            nums[decEle],nums[justGreater] = nums[justGreater],nums[decEle]
            
        self.reverse(nums,decEle+1)
        
    def reverse(self,nums,index):
        i = index
        j = len(nums)-1
        while i<j :
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1