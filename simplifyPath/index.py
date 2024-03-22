class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        new_path = path + "/"
        curr = ""
        for i in range(len(new_path)):
            if new_path[i] == "/":
                if curr == "..":
                    if len(stack) > 0:
                        stack.pop()
                elif curr != "." and curr != "":
                    stack.append(curr)
                curr = ""
            else:
                curr = curr + new_path[i]
        res = "/" + "/".join(stack)

        return res


Solution().simplifyPath("/../abc///./ab")
