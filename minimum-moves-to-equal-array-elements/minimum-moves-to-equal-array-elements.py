class Solution:
    def minMoves(self, arr: List[int]) -> int:
        arr.sort()
        self.size = len(arr)
        self.arr = arr
        self.moves = 0
        diff = arr[0]
        for i in range(1, self.size):
            diff = self.moves+self.arr[i] - self.arr[i-1]
            self.arr[i] += self.moves
            self.moves += diff
            # print(self.moves,diff)
        return (self.moves)

    def check_array(self):
        return len(set(self.arr)) != 1