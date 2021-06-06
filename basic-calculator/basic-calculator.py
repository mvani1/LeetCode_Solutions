class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        sums = 0
        j = -1
        for i in range(len(s)):
            if s[i].isdigit() and i>j:
                num = ""
                j = i
                while j < len(s) and s[j].isdigit():
                    num += s[j]
                    j+=1
                sums += int(num)*sign
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(sums)
                stack.append(sign)
                sums = 0
                sign = 1
            elif s[i] ==')':
                sums = stack.pop() * sums
                sums += stack.pop()
                
        return sums