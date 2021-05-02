class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        old = intervals[0][0]
        end = intervals[0][1]
        intervals.append([99999,0])
        for i in range(1,len(intervals)):
            # print(end)
            if end >= intervals[i][0]:
                end = max(end,intervals[i][1])
            else:
                result.append([old,end])
                old,end = intervals[i]
        return(result)
