class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = "aeiou"
        ans = 0
        unique = count = 1
        for i in range(1,len(word)):
            if word[i-1] <= word[i]:
                count +=1
                if word[i-1] < word[i]:
                    unique += 1
            else:
                count = 1
                unique = 1
            if unique == 5 :
                ans = max(ans,count)
        return (ans)