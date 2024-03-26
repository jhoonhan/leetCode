class Solution:
    def evalRPN(self, tokens: list) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for el in tokens:
            if el not in operators:
                stack.append(int(el))
            else:
                el2 = int(stack.pop())
                el1 = int(stack.pop())
                if el == "+":
                    stack.append(el1 + el2)
                elif el == "-":
                    stack.append(el1 - el2)
                elif el == "*":
                    stack.append(el1 * el2)
                else:
                    stack.append(int(el1 / el2))
        return stack[0]


Solution().evalRPN(["2", "1", "+", "3", "*"])
