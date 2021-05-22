class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hash_map = Counter(secret)
        cow = bull = 0
        for i in range(len(secret)):
            secretDigit, guessDigit = secret[i] , guess[i]
            if secretDigit == guessDigit:
                bull +=1
                hash_map[guessDigit] -= 1
                if hash_map[guessDigit] == 0:
                    del hash_map[guessDigit]
        for i in range(len(secret)):
            secretDigit, guessDigit = secret[i] , guess[i]
            
            if guessDigit != secretDigit and guessDigit in hash_map:
                if hash_map[guessDigit] == 0:
                    del hash_map[guessDigit]
                else:
                    hash_map[guessDigit] -= 1
                    cow+=1
                    
        return str(bull)+'A'+str(cow)+'B'
