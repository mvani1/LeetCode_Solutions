class Solution:
    def reverse(self, x: int) -> int:
        abso = abs(x)
        ranges = range(-2**31, 2**31 - 1)
        if x<0:
            imd = -1*(int(str(abso)[::-1]))
            return 0 if imd not in ranges else imd
        else:
            imd = (int(str(x)[::-1]))
            return 0 if imd not in ranges else imd