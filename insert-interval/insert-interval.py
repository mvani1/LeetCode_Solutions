class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort()
        
        output = []
        
        start = []
        
        for i in range(len(intervals)):
            if (output and output[-1][1] >= intervals[i][0]):
                start,end = output.pop()
                output.append([start,max(end,intervals[i][1])])
            else:
                output.append(intervals[i])
                
        return(output)