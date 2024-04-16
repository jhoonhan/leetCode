class Editor:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def append(self, w):
        for char in w:
            self.s1.append(char)
        self.s2.append(("append", w))
        print(f"Appended: {w}")
        print(self.s1)
        print("")

    def delete(self, k):
        popped = []
        for _ in range(k):
            if not self.s1:
                break
            popped.append(self.s1.pop())
        self.s2.append(("delete", "".join(popped[::-1])))
        print(f"Deleted: {popped[::-1]}")
        print(f"{self.s1}")
        print("")

    def print(self, k):
        if k > len(self.s1):
            return
        print(self.s1[k - 1])

    def undo(self):
        action, value = self.s2.pop()
        print("undoing:", action, value)
        print(self.s2)

        # print(self.s2)

        if action == "append":
            self.delete(len(value))
        elif action == "delete":
            self.append(value)
        print("")


# if __name__ == "__main__":
#     editor = Editor()
#     # get input
#     num_ops = input()
#     for row in range(int(num_ops)):
#         data = input()
#         commands = data.split(" ")

#         if commands[0] == "1":
#             editor.append(commands[1])
#         elif commands[0] == "2":
#             editor.delete(int(commands[1]))
#         elif commands[0] == "3":
#             editor.print(int(commands[1]))
#         elif commands[0] == "4":
#             editor.undo()

editor = Editor()

editor.append("abc")
editor.print(3)
editor.delete(3)
editor.append("xy")
editor.print(2)
editor.undo()
editor.undo()
editor.print(1)
