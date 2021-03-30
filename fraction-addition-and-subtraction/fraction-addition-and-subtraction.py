class Solution:
    def fractionAddition(self, ex: str) -> str:
        num = re.findall(r'[+-]\d+|\d+',ex)
        op = re.findall(r'[+-]',ex)
        
        j = 0
        while len(num)!=2:
            temp = num[0:4]
            num[0],num[1] = (self.calc(temp))
            if len(num)>2:
                for k in range(2,4):
                    num.pop(2)
            
        return str(num[0])+'/'+str(num[1])
            
    def calc(self,num):
        if num[1] != num[3]:
            lcm = int(self.lcm(int(num[1]),int(num[3])))
            num1 = int(num[0])*(lcm//int(num[1]))
            num2 = int(num[2])*(lcm//int(num[3]))
        else:
            lcm = int(num[1])
            num1 = int(num[0])
            num2 = int(num[2])
            
        final_num = num1+num2
        
        gcd = self.gcd(abs(final_num),abs(lcm))
        n,d = final_num//gcd,lcm//gcd
        return str(n),str(d)
        
    def gcd(self,a,b):
        if a == 0:
            return b
        return self.gcd(b % a, a)
 
    def lcm(self,a,b):
        return (a / self.gcd(a,b)) * b
        