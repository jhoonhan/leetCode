class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for char in s:
            if char not in map:
                stack.append(char)
            else:
                popped = stack.pop()
                if popped != map[char]:
                    print("Failed")
                    return False

        print("TRUE")
        return True


Solution().isValid("()[]{)}")
