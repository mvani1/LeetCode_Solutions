class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse = True,key = lambda x:(x[1],x[0]))
        print(boxTypes)
        maxx = 0
        value = 0
        for box,val in boxTypes:
            for i in range(box):
                maxx += 1
                value += val
                if maxx > truckSize:
                    maxx -=1
                    value -= val
        return value