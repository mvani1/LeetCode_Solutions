class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        result = []
        for i in nums:
            if i in result:
                return i
            else:
                result.append(i)