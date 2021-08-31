MAX = 2**31 -1
MIN = -2**31
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if (dividend < 0 and not divisor < 0) or (not dividend < 0 and divisor < 0):
            sign = '-'  
        elif (dividend < 0 and divisor < 0):
            sign = '+'
        else:
            sign = '+'
        if sign == '-':
            ans = math.ceil(dividend/divisor)
        else:
            ans = math.floor(dividend/divisor)
        if ans > MAX:
            return MAX
        elif ans < MIN:
            return MIN
        else:
            return ans  