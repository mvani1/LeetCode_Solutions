class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = self.remove_duplicate_stars(p)
        self.text_length = len(s)
        self.pattern_length = len(p)
        self.dp = {}
        return self.helper(s,p)
    
    def helper(self,text,pattern):
        dp = self.dp
        if (text,pattern) in dp:
            return dp[(text,pattern)]
        if text == pattern or pattern =='*':
            dp[(text,pattern)] =  True
        elif not text or not pattern: 
            dp[(text,pattern)] = False
        elif pattern[0] == text[0] or pattern[0] =='?':
            dp[(text,pattern)] =self.helper(text[1:],pattern[1:])
        elif pattern[0] == '*':
            dp[(text,pattern)] =self.helper(text,pattern[1:]) or self.helper(text[1:],pattern)
        else:
            dp[(text,pattern)] =False
        return dp[(text,pattern)] 
        
    def remove_duplicate_stars(self, p):
        if p == '':
            return p
        p1 = [p[0],]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1) 
#         if self.text_length<=t_idx and self.pattern_length <= p_idx:
#             return True
#         if (self.text_length<=t_idx and self.pattern_length > p_idx) or(self.text_length>t_idx and self.pattern_length <= p_idx) :
#             return False
#         if (pattern[p_idx] == '.') or (pattern[p_idx] == text[t_idx]):
#             if (self.pattern_length >p_idx and [p_idx+1] == '*'):
#                 return self.helpler(text,pattern,t_idx,p_idx)
#             else:
#                 return self.helper(text,pattern,t_idx+2,p_idx)
        
#         if (self.pattern_length >p_idx and [p_idx+1] == '*'):
#             return self.helpler(text,pattern,t_idx,p_idx)