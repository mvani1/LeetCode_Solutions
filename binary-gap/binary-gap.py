class Solution:
    def binaryGap(self, n: int) -> int:
        binary = str(bin(n)[2:])
        index = []
        for i in range(len(binary)):
            if binary[i] =='1':
                index.append(i)
        try:
            result = []
            for j in range(len(index)-1):
                result.append(index[j+1]-index[j])
            return max(result)
        except:return 0