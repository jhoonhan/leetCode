class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        self.min_val = val if self.min_val == None else min(val, self.min_val)
        new_node = {"val": val, "min_val": self.min_val}
        self.stack.append(new_node)

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) < 1:
            self.min_val = None
        else:
            self.min_val = self.getMin()

    def top(self) -> int:
        return self.stack[-1]["val"]

    def getMin(self) -> int:
        return self.stack[-1]["min_val"]


class MinStack_Neet:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
