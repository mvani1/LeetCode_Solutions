class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = []
        i=0
        while(True):
            if i>len(S)-1:
                break
            if len(S)-1 > i and S[i]==S[i+1]:
                S = S.replace(S[i]+S[i+1],"")
                i=-1
            i+=1
        return(S)
                
            