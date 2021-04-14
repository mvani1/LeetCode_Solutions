class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ss = collections.Counter(nums)
        for i,v in ss.items():
            if v >1:
                yield i