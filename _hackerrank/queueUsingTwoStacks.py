class Stack:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        self.s1.append(val)

    def __rearrange(self):
        while self.s1:
            self.s2.append(self.s1.pop())

    def dequeue(self):
        if not self.s2:
            self.__rearrange()

        return self.s2.pop()

    def peek(self):
        if not self.s2:
            self.__rearrange()

        res = self.s2[-1]
        print(res)
        return res


stack = Stack()

for _ in range(int(input())):
    query = input()
    if " " in query:
        if query.split()[0] == "1":
            stack.enqueue(query.split()[1])
    else:
        if query == "2":
            stack.dequeue()
        if query == "3":
            stack.peek()
