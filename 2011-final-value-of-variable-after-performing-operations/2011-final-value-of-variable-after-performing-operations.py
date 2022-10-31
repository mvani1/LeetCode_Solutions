class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            start, end = op[0], op[-1]
            if start == '+' or end == '+':
                # increment
                x += 1
            else:
                # decrement
                x -= 1
        return x