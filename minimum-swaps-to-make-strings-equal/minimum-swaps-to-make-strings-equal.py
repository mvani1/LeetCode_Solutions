

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        counts = Counter(s1 + s2)
        if counts['x'] % 2 == 1 or counts['y'] % 2 == 1:
            return -1
        xy, yx = 0, 0
        for i in range(len(s1)):
            if (s1[i] == 'x' and s2[i] == 'y'):
                xy += 1
            elif (s1[i] == 'y' and s2[i] == 'x'):
                yx += 1
        ans = xy//2 + yx//2+\
        xy%2+\
        yx%2
        return ans
        # minxy = min(xy, yx)
        # xy -= minxy
        # yx -= minxy
        # return minxy * 2 + (xy + yx) // 2
        