class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:(x[1]-x[0]))
        sumsA = 0
        sumsB = 0
        print(costs)
        for i in costs[:len(costs)//2]:
            sumsA +=i[1]
        for i in costs[len(costs)//2:]:
            sumsB +=i[0]
        return sumsA+sumsB
                   