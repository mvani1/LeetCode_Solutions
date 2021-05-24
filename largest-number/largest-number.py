class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ''.join(sorted(map(str, nums), key=LargerNumKey)) 
        return (res) if res[0] !='0' else '0'