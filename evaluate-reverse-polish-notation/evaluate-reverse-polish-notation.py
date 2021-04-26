class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ['+','-','*','/']
        ops = []
        for i in tokens:
            if i not in operator:
                stack.append(i)
            else:
                ops.append(i)
            while ops:
                b,a = stack.pop(),stack.pop()
                op = ops.pop()
                stack.append(int(eval(str(a)+str(op)+str(b))))
        return int(stack[0])
