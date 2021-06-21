class Solution:
    def entityParser(self, text: str) -> str:
        if ';' not in text:
            return text
        j = 0
        self.res = ""
        while j < len(text):
            if text[j] == '&' and j+1 < len(text) and text[j+1]!= '&':
                i = j 
                temp = ""
                while text[j]!=';':
                    temp += text[j]
                    j+=1
                self.find(temp+';')
            else:
                self.res += text[j]
            j+=1
        return (self.res)
    def find(self,text):
        
        if text == '&quot;':
            self.res += '\"'
        elif text == '&apos;':
            self.res += '\''
        elif text == '&amp;':
            self.res += '&'
        elif text == '&gt;':
            self.res += '>'
        elif text == '&lt;':
            self.res += '<'
        elif text == '&frasl;':
            self.res += '/'
        else:
            self.res += text
        
