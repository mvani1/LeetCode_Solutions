class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res,dups = set(),set()
        seen = {}
        for i,val in enumerate(nums):
            if val not in dups:
                dups.add(val)
                for ii,val2 in enumerate(nums[i+1:]):
                    com = -val - val2
                    if com in seen and seen[com] == i:
                        res.add(tuple(sorted((val,val2,com))))
                    seen[val2] = i
        return res