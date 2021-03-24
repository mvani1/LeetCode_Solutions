class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(set(s))==len(s):
            return len(s)
        res=[0]
        for i in range(len(s)):
            temp = s[i]
            for j in range(i+1,len(s)):
                if s[j] in temp:
                    break
                temp+=(s[j])
            res.append(len(temp))

        return (max(res))