class Solution:
    def maxDepth(self, s: str) -> int:
        if len(s)==1:
            return 0
        stack,count = [],0
        minn = -1
        for i in range(len(s)):
            if s[i] =='(':
                count+=1
            elif s[i]==')':
                count-=1
            if count>minn:
                minn=count
        return (minn)
            
        