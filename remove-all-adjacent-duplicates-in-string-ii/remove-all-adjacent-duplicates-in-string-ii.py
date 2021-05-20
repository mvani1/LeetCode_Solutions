class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        curr = ""
        count = 0
        
        for char in s + " ":
            while char != curr:
                if count and count % k == 0:
                    if stack:
                        curr, count = stack.pop()
                    else:
                        curr, count = "", 0
                else:
                    stack.append((curr, count%k))
                    curr, count = char, 0
            count += 1
            
        return "".join([ char * count for char, count in stack ]).strip()
#         stack = []
#         for i in s:
#             if stack and stack[-1][0] == i:
#                 stack[-1][1]+=1
#             else:
#                 stack.append([i,1])
#             if stack and stack[-1][1] == k:
#                 stack.pop()
#         res = ''
#         for i,v in stack:
#             res += i*v
#         return res
            