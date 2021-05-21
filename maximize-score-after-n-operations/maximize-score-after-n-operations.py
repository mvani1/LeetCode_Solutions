class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def getBit(mask, i):
            return (mask >> i) & 1

        def setBit(mask, i):
            return (1 << i) | mask

        @lru_cache(None)
        def gcd(x, y):
            return math.gcd(x, y)

        @lru_cache(None)
        def dp(op, mask):
            if op == n + 1:  # Reach to n operations
                return 0

            ans = 0
            for i in range(2 * n):
                if getBit(mask, i) == 1: continue
                for j in range(i + 1, 2 * n):
                    if getBit(mask, j) == 1: continue
                    newMask = setBit(setBit(mask, i), j)  # Mark as used i and j elements
                    ans = max(ans, dp(op + 1, newMask) + op * gcd(nums[i], nums[j]))
            return ans

        n = len(nums) // 2
        return dp(1, 0)