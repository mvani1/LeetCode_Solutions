class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn,maxx =9999999,0
        abss=[]
        for i in range(len(prices)):
            if minn>prices[i]:
                minn = prices[i]
                maxx = max(prices[i:])
                abss.append(maxx-minn)
        return max(abss)