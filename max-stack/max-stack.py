class MaxStack:
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self._data = []


	def push(self, x: int) -> None:
		self._data.append(x)

	def pop(self) -> int:
		return self._data.pop()

	def top(self) -> int:
		return self._data[-1]

	def peekMax(self) -> int:
		return max(self._data)

	def popMax(self) -> int:
		target = max(self._data)
		for index in range(len(self._data)-1, -1, -1):
			if self._data[index] == target:
				return self._data.pop(index)