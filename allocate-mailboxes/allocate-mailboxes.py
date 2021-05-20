class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        B = [0]
        # B[i] = A[0] + A[1] + A[2] + .. + A[i-1]
        for i, a in enumerate(houses):
            B.append(B[i] + a)
# between A[i]~A[j] with only one mailbox.

# Initialy, when k = 1, dp[i] = cal(0, i)
# when we increment k, we can update dp with one more mailbox added.
        def cal(i, j):
            '''
                # cal(i, j) will return the minimum distance,
            '''
            m1, m2 = (i + j) // 2, (i + j + 1) // 2
            return (B[j + 1] - B[m2]) - (B[m1 + 1] - B[i])

        #dp[i] will means that,
        #the minimum distance of i + 1 first house.
        dp = [cal(0, j) for j in range(n)]
        print(dp)
        
        for k in range(2, k + 1):
            for j in range(n - 1, k - 2, -1):
                for i in range(k - 2, j):
                    dp[j] = min(dp[j], dp[i] + cal(i + 1, j))
        return int(dp[-1])