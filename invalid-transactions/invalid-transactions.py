class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        for i in transactions:
            temp = i.split(',')
            if int(temp[2])>1000:
                yield (i)
            else:
                for j in transactions:
                    temp2 = j.split(',')
                    if temp[0]==temp2[0] and temp[3]!=temp2[3] and abs(int(temp[1])-int(temp2[1]))<61:
                        yield (i)
                        break

                        
        
            