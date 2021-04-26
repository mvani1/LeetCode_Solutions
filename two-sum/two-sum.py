class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}
        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target in hash_set:
                return [hash_set.get(new_target),i]
            hash_set[nums[i]] = i