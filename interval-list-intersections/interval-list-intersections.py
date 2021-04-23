class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        res = []
        first = firstList
        second = secondList
        if  not first or not second:return res
        for i in range(len(firstList)):
            for j in range(len(secondList)):
                if (first[i][1]>=second[j][0] and first[i][0]<= second[j][0]) or (second[j][1]>=first[i][0] and second[j][0]<= first[i][0]):

                    res.append([max(first[i][0],second[j][0]),min(first[i][1],second[j][1])])
        return (res)