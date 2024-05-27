class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in char_map:
                if len(stack) == 0:
                    return False

                prev = stack.pop()

                if char_map[char] != prev:
                    return False

            else:
                stack.append(char)

        if len(stack) > 0:
            return False
        else:
            return True


Solution().isValid("(){}")
