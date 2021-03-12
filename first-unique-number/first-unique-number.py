class FirstUnique:

    def __init__(self, nums: List[int]):
        self.result = nums
        self.hash = {}
        for i in nums:
            self.hash[i] = self.hash.get(i,0)+1


    def showFirstUnique(self) -> int:
        for i,v in self.hash.items():
            if v == 1:
                return i
        return -1

    def add(self, value: int) -> None:
        self.hash[value] = self.hash.get(value,0)+1

        self.result.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)