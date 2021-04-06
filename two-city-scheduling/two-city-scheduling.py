class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:(x[1]-x[0]))
        sums = 0
        n = len(costs)
        for i in range(n//2):
            sums+= costs[i][1]
        for i in range(n//2,n):
            sums+= costs[i][0]
        
        return(sums)
        