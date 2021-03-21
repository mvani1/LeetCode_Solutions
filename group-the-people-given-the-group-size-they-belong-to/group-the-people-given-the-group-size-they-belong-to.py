class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hash_map = {}
        
        for i in groupSizes:
            hash_map[i]=hash_map.get(i,0)+1
        
        groups = {x:[[]] for x in hash_map}
        
        for index,ele in enumerate(groupSizes):
            if ele in groups:
                if len(groups[ele][-1]) == ele:
                    groups[ele].append([index])
                else:
                    groups[ele][-1].append(index)
                    
            else:
                groups[ele][-1].append([index])
                
        res = []
        for i in groups.values():
            res.extend(i)
        return res
                