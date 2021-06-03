class Solution:
    def canConvert(self, s1, s2):
        if s1 == s2: return True
        dp = {}
        for i, j in zip(s1, s2):
            print(dp)
            if dp.setdefault(i, j) != j:
                return False
        return len(set(s2)) < 26