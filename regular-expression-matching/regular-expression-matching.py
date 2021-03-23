class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        st = re.findall(p,s)
        if s in st:
        # print(st)
            return True
        return False