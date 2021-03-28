class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic =  {}  
        
        for item in items:
            if item[0] in dic:
                dic[item[0]].append(item[1])
            else:
                dic[item[0]] = [item[1]]
        
        def sort_avg(list):   
            list = sorted(list, reverse = True)
            return int(sum(list[0:5])/5)
        
        final = []
        
        for item in dic:  
            final.append([item, sort_avg(dic[item])])
        final.sort()
        return final
        
        