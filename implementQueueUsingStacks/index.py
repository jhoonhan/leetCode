class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:
    def __init__(self):
        self.top = None
        self.tail = None

    def print(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, x: int) -> None:
        new_node = Node(x)
        if self.top == None:
            self.top = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self) -> int:
        if self.top is not None:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        else:
            return 0

    def peek(self) -> int:
        if self.top is not None:
            return self.top.value
        else:
            return 0

    def empty(self) -> bool:
        return self.top == None


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


queue = MyQueue()

queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
print(queue.pop())
queue.push(5)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())


queue.print()
