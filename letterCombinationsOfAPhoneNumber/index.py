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

        # digits = 23
        def backtrack(i, acc):
            # 0, 2, ""
            # 1, 3, "a"
            ## 2, N, "ad"
            ## 2, N, "ae"
            ## 2, N, "af"
            # 1, 3, "b"
            ## 2, N, "bd"
            if len(acc) == len(digits):
                # none
                # none
                ## res = ["ad"]
                ## res = ["ad", "ae"]
                ## res = ["ad", "ae", "af"]
                # none
                ## res = ["ad", "ae", "af", "bd"]
                res.append(acc)
                return
            for c in digitToChar[digits[i]]:
                # a,b,c
                ## d,e,f
                ## e,f
                ## f
                ##
                # b,c
                ## d,e,f
                ## e,f
                backtrack(i + 1, acc + c)

        if digits:
            backtrack(0, "")
        print(res)

        return res
