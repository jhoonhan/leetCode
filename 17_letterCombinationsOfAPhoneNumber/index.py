class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        def backtrack(i, acc):

            if len(acc) == len(digits):
                res.append(acc.copy())
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, acc + c)

        if digits:
            backtrack(0, "")
        print(res)

        return res
