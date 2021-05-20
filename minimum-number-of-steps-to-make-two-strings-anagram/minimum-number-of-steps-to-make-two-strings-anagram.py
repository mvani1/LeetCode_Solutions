class Solution:
    def minSteps(self, s: str, t: str) -> int:
        '''
        Time: O(n), space: O(1) n = len(s)+len(t)
        '''
        sss = set(s+t)
        ret = 0
        for c in sss:
            # c = chr(ord('a') + i)
            sc = s.count(c)
            tc = t.count(c)
            if sc > tc:
                ret += sc - tc
        
        return ret