# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # finding the peak
        self.lenMountain = mountain_arr.length()-1
        self.peak = self.peak(target,mountain_arr)
        print(self.peak)
        left = self.leftSearch(target,mountain_arr)
        if left!=-1:
            return left
        right = self.rightSearch(target,mountain_arr)
        if right!=-1:
            return right
        return -1
    
    def rightSearch(self,target,mountain_arr):
        left, right = self.peak,self.lenMountain
        while left<=right:
            mid = (left+right)//2
            mid_ele = mountain_arr.get(mid)
            if mid_ele == target:
                return mid
            elif mid_ele < target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def leftSearch(self,target,mountain_arr):
        left, right = 0, self.peak
        while left<=right:
            mid = (left+right)//2
            mid_ele = mountain_arr.get(mid)
            if mid_ele == target:
                return mid
            elif mid_ele < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def peak(self,target,mountain_arr):
        left, right = 0, self.lenMountain
        while left<right:
            mid = (left+right)//2
            mid_ele = mountain_arr.get(mid)
            if mid_ele < mountain_arr.get(mid+1):
                left = mid + 1 
            else:
                right = mid - 1
        return(left)