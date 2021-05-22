class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left,right = k-1, len(cardPoints)-1
        if k == len(cardPoints):
            return sum(cardPoints)
        maxSum = sum(cardPoints[:k])
        total = maxSum
        while left >= 0:
            maxSum -= cardPoints[left]
            maxSum += cardPoints[right]
            total = max(total,maxSum)
            right -=1
            left -= 1
        return total