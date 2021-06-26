class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = [(-box[1],box[0]) for box in boxTypes]
        heapq.heapify(heap)
        # boxTypes.sort(reverse = True,key = lambda x:(x[1],x[0]))
        maxx = 0
        value = 0
        while heap and maxx !=truckSize:
            val,box = heapq.heappop(heap)
            for i in range(box):
                maxx += 1
                value += -val
                if maxx > truckSize:
                    maxx -=1
                    value -= -val
        return value
        # for box,val in boxTypes:
        #     for i in range(box):
        #         maxx += 1
        #         value += val
        #         if maxx > truckSize:
        #             maxx -=1
        #             value -= val
        # return value