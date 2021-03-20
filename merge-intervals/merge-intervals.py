class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        temp = []
        for i in intervals:
            if i not in temp:
                temp.append(i)
        intervals = temp
        # intervals.sort()
        i=0
        while i+1 < len(intervals):
            intervals.sort()
            
            curr,nex = intervals[i],intervals[i+1]
            start,end = intervals[i][0],intervals[i+1][1]
            if start < end and curr[1] >= nex[0]:
                intervals.pop(i)
                intervals.pop(i)
                if end > curr[1]:
                    intervals.append([start,end])
                else:
                    intervals.append([start,curr[1]])
                    
                i=0
            else:
                i+=1
        return intervals