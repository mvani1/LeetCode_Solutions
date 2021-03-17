class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        h = dict(zip(string.ascii_lowercase,widths))
        sums=0
        temp = ""
        out = []
        for i in range(len(s)):
            sums += h[s[i]]
            temp += s[i]
            if sums>100:
                sums = h[s[i]]
                out.append(temp)
                temp = s[i]
        out.append(temp)
        
        return [len(out),sums]
            