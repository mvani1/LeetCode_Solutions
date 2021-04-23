class Solution:
    '''
        Time Complexity = O(n)
    '''
    def firstUniqChar(self, s: str) -> int:
        # boolean = [0 for _ in range(256)]
        hash_map = {}
        h = {}
        minimum = (float('inf'),float('inf'))
        visited = set()
        for v,i in enumerate(s):
            hash_map[i] = hash_map.get(i,0)+1
            if hash_map[i]==1 and i not in visited:
                h[(i,hash_map[i])] = v
                visited.add(i)
            elif hash_map[i]>1 and (i,hash_map[i]-1) in h and  i in visited:
                del h[(i,hash_map[i]-1)]
        
        return list(h.items())[0][1] if h.items() else -1