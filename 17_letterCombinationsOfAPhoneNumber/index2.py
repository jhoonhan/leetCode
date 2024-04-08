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

        def dfs(num, acc):
            for char in digitToChar[num]:
                print(char)

        for num in digits:
            dfs(num, "")


Solution().letterCombinations("23")
