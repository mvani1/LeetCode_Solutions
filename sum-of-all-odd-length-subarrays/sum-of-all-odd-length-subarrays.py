class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sums = sum(arr)
        j = 0
        for i in range(3,len(arr)+1,2):
            temp = i
            for j in range(len(arr)):
                if len(arr[j:i]) == temp:
                    sums+=sum(arr[j:i])
                i+=1
        return(sums)