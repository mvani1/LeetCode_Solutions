class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start+i*2 for i in range(n)]
        sums = nums[0]
        for j in range(1,len(nums)):
            sums = sums ^ nums[j]
        return sums