class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        self.map = dict(zip(map(str,range(0,26)),range(0,26)))
        rmap = dict(zip(range(0,26),map(str,range(0,26))))
        if num1 =='0' or num2 == '0':
            return '0'
        num = self.convert(num1) * self.convert(num2)
        res = ""
        while num:
            temp = num%10
            res = rmap[temp] + res
            num //= 10
        return (res)
        # return a*b

    def convert(self,num):
        number = 0
        for i in num:
            number = number*10 + self.map[i]
        return number
