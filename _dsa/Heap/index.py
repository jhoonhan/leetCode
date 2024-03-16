class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_childe(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


mheap = MaxHeap()
mheap.insert(99)
mheap.insert(72)
mheap.insert(61)
mheap.insert(58)

print(mheap.heap)


mheap.insert(100)

print(mheap.heap)

mheap.insert(75)
print(mheap.heap)
