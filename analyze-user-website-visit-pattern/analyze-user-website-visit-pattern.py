from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        UTW = tuple(zip(username, timestamp, website))
        sorted_utw = sorted(UTW)
        usernames = defaultdict(list)
        
        for u,t,w in sorted_utw:
            usernames[u].append(w)
        
        pattern_count = defaultdict(int)
        
        for user,value in usernames.items():
            combs = set(combinations(value, 3))
            for comb in combs:
                pattern_count[comb] = pattern_count[comb]+1
        
        a = sorted(pattern_count,key=lambda x:(-pattern_count[x],x))
        return(a[0])
            