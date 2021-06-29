class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[0][0] = True
        for i in range(1,len(dp[0])):
            if pattern[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if text[i-1] == pattern[j-1] or pattern[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if (pattern[j-2] == '.' or pattern[j-2] == text[i-1]):
                        dp[i][j] = dp[i][j] | dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]
        
        
        
        
        # memo = {}
        # def dp(i,j):
        #     if(i,j) not in memo:
        #         if j == len(pattern):
        #             ans = i == len(text)
        #         else:
        #             first_match = i<len(text) and pattern[j] in {text[i],'.'}
        #             if j+1 < len(pattern) and pattern[j+1] == '*':
        #                 ans = dp(i,j+2) or first_match and dp(i+1,j)
        #             else:
        #                 ans = first_match and dp(i+1,j+1)
        #         memo[i,j] = ans
        #     return memo[i,j]
        # return dp(0,0)