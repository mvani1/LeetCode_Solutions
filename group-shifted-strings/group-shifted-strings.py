class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        '''
        To identify each group, compute the modulo 26 difference between each letter in a word with the first letter in it.
        '''
        hashmap = {}
        for s in strings:
            key = ()
            for i in range(len(s) - 1):
                circular_difference = 26 + ord(s[i+1]) - ord(s[i])
                key += (circular_difference % 26,)
            hashmap[key] = hashmap.get(key, []) + [s]
        return list(hashmap.values())