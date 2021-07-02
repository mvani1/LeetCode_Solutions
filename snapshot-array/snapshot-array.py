class SnapshotArray:

    def __init__(self, length: int):
        self.h =defaultdict(defaultdict)
        self.cap = 0

    def set(self, index: int, val: int) -> None:
        self.h[self.cap][index] = val

    def snap(self) -> int:
        self.cap += 1
        return self.cap - 1

    def get(self, index: int, snap_id: int) -> int:
        curr = snap_id
        while curr >0 and index not in self.h[curr]:
            curr -= 1
        if index in self.h[curr]:
            return self.h[curr][index]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)