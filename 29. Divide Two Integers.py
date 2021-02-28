class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ranges = range(-2**31,(2**31))
        if dividend <0 and divisor<0:
            ans = floor(dividend/divisor)
            return ans if ans in ranges else (2**31)-1
        if dividend <0 or divisor <0:
            ans = ceil(dividend/divisor)
            return ans if ans in ranges else (2**31)-1
        ans = floor(dividend/divisor)
        return ans if ans in ranges else (2**31)-1