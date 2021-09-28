class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        hash_1 = Counter(arr1)
        hash_3 = Counter(arr3)        
        hash_2 = Counter(arr2)        
        result = []
        for ele in hash_1:
            if hash_2.get(ele, False) and hash_3.get(ele, False):
                result.append(ele)
        return result