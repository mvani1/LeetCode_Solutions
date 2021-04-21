class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        left = 0
        right = 0
        last = {v:i for i,v in enumerate(S)}
        result = []
        for i in S:
            new = i
            right = last[new]
            old = left
            while left<=right:
                if last[S[left]] > right:
                    right = last[S[left]]
                left+=1
            subs = S[old:right+1]
            if subs:
                result.append(len(subs))
            right+=1
        return result
                    