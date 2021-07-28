class Solution:
    def __init__(self):
        self.map = {}
        
    def isScramble(self, S1: str, S2: str) -> bool:
        n = len(S1)

        # Empty strings are scramble strings
        if not n:
            return True

        if S1+S2 in self.map:
            return self.map.get(S1+S2)
        
        # Equal strings are scramble strings
        if S1 == S2:
            return True

        # Check for the condition of anagram
        if not self.check(S1,S2):
            return False

        for i in range(1, n):
            
            if (self.isScramble(S1[:i], S2[:i]) and\
            self.isScramble(S1[i:], S2[i:])):
                return True
            if (self.isScramble(S1[-i:], S2[:i]) and\
            self.isScramble(S1[:-i], S2[i:])):
                return True
        self.map[S1+S2] = False
        return False
    
    def check(self,s1,s2):
        if len(s1) != len(s2):
            return False
        a = Counter(s1)
        b = Counter(s2)
        return a == b