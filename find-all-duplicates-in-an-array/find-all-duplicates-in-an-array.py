class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        fre_counter = {}
        for i in nums:
            fre_counter[i] = fre_counter.get(i,0)+1
            if fre_counter[i] == 2:
                yield i
        # print(fre_counter)