class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        Time  : O(N)
        Space : O(N)
        '''
        counter = collections.Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i]<s[pos]:pos=i
            counter[s[i]] -=1
            if counter[s[i]]==0:break
                #Found the minimum leftmost element
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos],"")) if s else ""
        