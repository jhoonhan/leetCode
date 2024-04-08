class Solution:
    def letterCombinations(self, digits: str) -> list:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtracK(i, acc):
            if len(acc) == len(digits):
                res.append(acc)
                return
            for char in digitToChar[digits[i]]:
                backtracK(i + 1, acc + char)

        if digits:
            backtracK(0, "")

        return res
