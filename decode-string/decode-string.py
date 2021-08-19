class Solution:
    def decodeString(self, s: str) -> str:
        if not s:return s
        stack = []
        string = ""
        final = ""
        open =1
        for i in s:
            if i =='[':
                open += 1
            if i == ']':
                temp = ""
                while stack and not stack[-1].isdigit():
                    popped = stack.pop()
                    if popped == '[': continue
                    temp = popped + temp
                digit = ""
                while stack:
                    popped = stack.pop()
                    if not popped.isdigit():
                        stack.append(popped)
                        break
                    else:
                        digit = popped + digit
                if open:
                    stack.append(temp * int(digit))
                else:
                    final = temp * digit
            else:
                stack.append(i)
        return "".join(stack)