class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left,right = 0 ,0 
        temp = ''
        h = {}
        p_h = Counter(p)
        ans = []
        target = 0
        while right<len(s):
            target +=1
            temp+=s[right]
            while target == len(p):
                if p_h == Counter(temp):
                    ans.append(left)
                target-=1
                temp = temp[1:]
                left +=1
            right+=1
        return ans