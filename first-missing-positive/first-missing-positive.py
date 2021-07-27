class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        f = collections.Counter(nums)
        count =1
        while f.get(count,0):
            count+=1
        return count
        