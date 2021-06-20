class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        mapp = {}
        i = 0
        maxx = float('-inf')
        for j in range(len(s)):
            mapp[s[j]] = mapp.get(s[j],0) + 1
            while len(mapp) > k:
                mapp[s[i]] -= 1
                if s[i] in mapp and mapp[s[i]] == 0:
                    del mapp[s[i]]
                i += 1
            maxx = max(maxx,j-i+1)
        return maxx