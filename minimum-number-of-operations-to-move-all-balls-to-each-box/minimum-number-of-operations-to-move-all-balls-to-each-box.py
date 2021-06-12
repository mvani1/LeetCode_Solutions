class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        findZeroes = [i for i,v in enumerate(boxes)]
        ans = [int(i) for i in boxes]
        
        def findOp(initial):
            ans = 0
            for i,v in enumerate(boxes):
                if i == initial : continue
                if v == '1':
                    ans += (abs(initial-i))
            return ans
        for i in findZeroes:
            ans[i] = findOp(i)
        return (ans)