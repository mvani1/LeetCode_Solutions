class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indexs = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                indexs.append(i)
        res = []
        for j in range(len(boxes)):
            temp = []
            for k in indexs:
                if k!=j:
                    temp.append(abs(j-k))
            res.append(sum(temp))
        return res