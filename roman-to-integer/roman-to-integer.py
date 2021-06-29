values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
class Solution:
    def romanToInt(self, s: str) -> int:
        start = 0 
        total = 0
        while start < len(s):
            if start+1 < len(s) and values[s[start]] < values[s[start+1]]:
                total += values[s[start+1]] - values[s[start]]
                start+=1
            else:    
                total += values[s[start]]
            start += 1
        return(total)