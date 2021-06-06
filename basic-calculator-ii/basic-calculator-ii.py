class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(' ','')
        sums = 0
        sign = 1
        char = ''
        stack = []
        j=-1
        for i in range(len(s)):
            if s[i].isdigit() and i>j:
                temp = ''
                j = i
                while j<len(s) and s[j].isdigit():
                    temp += s[j]
                    j+=1
                if temp :
                    stack.append(int(temp)*sign)
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '*':
                temp = ''
                j = i+1
                while j<len(s) and s[j].isdigit():
                    temp += s[j]
                    j+=1
                stack.append(stack.pop()*int(temp))
                sums = 0
                sign = 1
            elif s[i] =='/':
                temp = ''
                j = i+1
                while j<len(s) and s[j].isdigit():
                    temp += s[j]
                    j+=1
                num = stack.pop()
                if num<0:
                    res = (-1*num) // int(temp)
                    res = -res 
                else:
                    res = num // int(temp)
                stack.append(res)
                sums = 0
        return sum(stack)