class Solution:
    def isValid(self, s: str) -> bool:
        map = {"}": "{", "]": "[", ")": "("}
        stack = []

        if len(s) % 2 != 0:
            return False
        if s[0] in map:
            return False

        for char in s:
            if char not in map:
                stack.append(char)
            else:
                if not stack or stack[-1] != map[char]:
                    return False
                else:
                    stack.pop()

        return True if not stack else False


aang = Solution()

aang.isValid("(){}}{")
