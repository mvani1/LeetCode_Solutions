class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        j = 0
        total = 0
        n = len(nums)
        min_count = n + 1

        for i in range(n):
            total += nums[i]
            while total >= s:
                new_count = i - j + 1
                if min_count > new_count:
                    min_count = new_count
                total -= nums[j]
                j += 1

        return 0 if min_count > n else min_count
                    