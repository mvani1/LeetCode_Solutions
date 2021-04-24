from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = []
        sorted_nums = SortedList(nums)
        for n in nums:
            i = sorted_nums.index(n)
            counts.append(i)
            sorted_nums.remove(n)
        return counts