class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        dups = set()
        seen = {}
        for i, val in enumerate(nums):
            if val not in dups:
                dups.add(val)
                for j in range(i+1,len(nums)):
                    comp = - val - nums[j]
                    if comp in seen and seen[comp] ==i:
                        res.add(tuple(sorted((val,nums[j],comp))))
                    seen[nums[j]] = i
        return res