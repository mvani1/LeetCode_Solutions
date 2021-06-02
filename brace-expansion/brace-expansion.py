class Solution:
    def expand(self, s: str) -> List[str]:
        self.res = []
        def back(s,word):
            if not s:
                self.res.append(word)
            else:
                if s[0] == '{':
                    i = s.find('}')
                    for letter in s[1:i].split(','):
                        back(s[i+1:],word+letter)
                else:
                    back(s[1:],word+s[0])
        back(s,'')
        self.res.sort()
        return (self.res)
            