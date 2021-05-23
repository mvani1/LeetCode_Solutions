class Solution:
    def minSwaps(self, data: List[int]) -> int:
        windowSize = sum(data)
        if windowSize <= 1 :
            return 0
        left , right = 0,windowSize-1
        size = float('inf')
        count = sum(data[:windowSize])
        while right<len(data):
            size = min(size , windowSize - count)
            count -= data[left]
            left  +=1
            right +=1
            if right <len(data):
                count += data[right]
        return (size)