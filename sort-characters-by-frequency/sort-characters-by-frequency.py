class Solution:
    def frequencySort(self, s: str) -> str:
        freq_Counter = collections.Counter(s)
        # print(freq_Counter)
        max_fre = max(freq_Counter.values())
        bucket = [[] for _ in range(max_fre+1)]
        for c,i in freq_Counter.items():
            bucket[i].append(c)
        string_builder = []
        # print(bucket)
        for i in range(len(bucket)-1,0,-1):
            for c in reversed(bucket[i]):
                string_builder.extend(c*i)
        return "".join(string_builder)
            