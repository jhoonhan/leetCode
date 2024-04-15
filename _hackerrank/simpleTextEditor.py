import collections


class Editor:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = collections.deque()

    def append(self, w):
        for char in w:
            self.s1.append(char)
        self.s2.append(("append", len(w)))

    def delete(self, k):
        popped = ""
        for _ in range(k):
            if not self.s1:
                return
            popped = self.s1.pop() + popped
        self.s2.append(("delete", popped))

    def print(self):
        print("".join(self.s1))

    def undo(self):
        action, value = self.s2.pop()
        if action == "append":
            self.delete(value)
        elif action == "delete":
            self.s1.append(value)


# if __name__ == "__main__":
#     editor = Editor()
#     # get input
#     num_ops = input()
#     for row in range(int(num_ops)):
#         data = input()
#         commands = data.split(" ")

#         if commands[0] == "1":
#             editor.append(commands[0])
#         elif commands[0] == "2":
#             editor.delete(int(commands[1]))
#         elif commands[0] == "3":
#             print("leggo")

#             editor.print()
#         elif commands[0] == "4":
#             editor.undo()

editor = Editor()

editor.append("abc")

editor.delete(2)
editor.print()

editor.undo()
editor.print()

editor.delete(1)
editor.print()
