class Solution:
    def intToRoman(self, num: int) -> str:
        integer = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        hash_map = dict(zip(integer,roman))
        result = ""
        # print(divmod(58, 1))
        for i in range(len(integer)-1,-1,-1):
            q,remain = divmod(num,integer[i])
            # print(q,remain)
            if q >= 1:
                result += hash_map[integer[i]]*(num//integer[i])
                num = remain
                
            if remain == 0:
                result += hash_map[integer[i]]*(num//integer[i])
                break
        return(result)
            