class Solution:
    def findMin(self, nums: List[int]) -> int:
        peak_index = 0
        nums = [0]+nums
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]<nums[i+1]:
                continue
            else:
                peak_index = i
                break
        # if not peak_index:return nums[0]
        print(peak_index)
        first = nums[1]
        second = nums[peak_index+1]
        if first>second:
            return second
        else:
            return first