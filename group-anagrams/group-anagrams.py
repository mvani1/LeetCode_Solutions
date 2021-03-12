class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = collections.defaultdict(list)
        
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in hs:
                hs[sorted_i].append(i)
            else:
                hs[sorted_i]= [i]
                
        return (hs.values())
