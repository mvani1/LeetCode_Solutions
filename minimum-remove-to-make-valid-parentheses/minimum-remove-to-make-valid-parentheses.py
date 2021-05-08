class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
#         stack = []
#         brackets = self.checker(s)
#         if not brackets[0]: return s
#         if brackets[1]>0:
#             bracket = '('
#         else:
#             bracket = ')'
#         for i in range(len(s)):
#             new_string = s[:i]+s[i+1:]
#             if s[i] == bracket:
#                 if not self.checker(new_string)[0]:return new_string
#         return ""
        open_stack , close_stack = [] , []
    
        for i in range(len(s)):
            if s[i] == '(':
                open_stack.append(i)
            if s[i] == ')':
                if open_stack:
                    open_stack.pop()
                else:
                    close_stack.append(i)
        stack = set(open_stack+close_stack)
        new = ""
        left = 0
        for i in range(len(s)):
            if i not in stack:
                new+=s[i]
        return new
        
        
    def checker(self,s):
        open = 0
        for i in range(len(s)):
            if s[i] == '(':
                open += 1
            if s[i] == ')':
                open -=1
            if open<0:
                return [True,open]
        if open:
            return [True,open]
        return [False]