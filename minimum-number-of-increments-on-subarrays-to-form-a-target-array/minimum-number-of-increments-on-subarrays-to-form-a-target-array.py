class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        result = target[0]
        prev = target[0]
        for i in target[1:]:
            if i > prev:
                result += i - prev
                
            prev = i
        return result