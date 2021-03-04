class Solution:
    def removeDuplicates(self, s: str) -> str:
        new_length = 0
        length = len(s)
        while length != new_length:
            new_length = len(s)
            unique = set(s)
            for i in unique:
                s=s.replace(2*i,"")
            length = len(s)
        return s